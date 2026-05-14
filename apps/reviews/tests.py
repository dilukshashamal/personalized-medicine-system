from django.contrib.auth import get_user_model
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils import timezone
from rest_framework import serializers
from django.test import TestCase

from apps.api.serializers import ClinicalReviewSerializer
from apps.audit.models import AuditEvent
from apps.patients.models import PatientProfile
from apps.recommendations.models import TreatmentRecommendation
from apps.recommendations.admin import TreatmentRecommendationAdmin
from apps.reviews.models import ClinicalReview


class ClinicalReviewSerializerTests(TestCase):
	def setUp(self):
		self.user = get_user_model().objects.create_user(
			username='reviewer',
			email='reviewer@example.com',
			password='safe-password-123',
		)
		self.patient = PatientProfile.objects.create(external_id='P-2001')
		self.recommendation = TreatmentRecommendation.objects.create(
			patient=self.patient,
			title='Review candidate',
			summary='Summary',
			rationale='Rationale',
		)

	def test_override_requires_reason(self):
		serializer = ClinicalReviewSerializer(
			data={
				'recommendation': self.recommendation.id,
				'reviewer': self.user.id,
				'decision': ClinicalReview.Decision.OVERRIDDEN,
				'limitations_acknowledged': True,
				'missing_data_acknowledged': True,
				'reviewed_at': timezone.now(),
			}
		)

		with self.assertRaises(serializers.ValidationError):
			serializer.is_valid(raise_exception=True)

	def test_approval_requires_acknowledgements(self):
		serializer = ClinicalReviewSerializer(
			data={
				'recommendation': self.recommendation.id,
				'reviewer': self.user.id,
				'decision': ClinicalReview.Decision.APPROVED,
				'reviewed_at': timezone.now(),
			}
		)

		self.assertFalse(serializer.is_valid())
		self.assertIn('limitations_acknowledged', serializer.errors)

	def test_review_update_creates_audit_event(self):
		review = ClinicalReview.objects.create(recommendation=self.recommendation)
		review.reviewer = self.user
		review.decision = ClinicalReview.Decision.APPROVED
		review.limitations_acknowledged = True
		review.missing_data_acknowledged = True
		review.save()
		self.recommendation.refresh_from_db()

		self.assertEqual(self.recommendation.status, TreatmentRecommendation.Status.APPROVED)
		self.assertIsNotNone(review.reviewed_at)
		self.assertTrue(
			AuditEvent.objects.filter(
				recommendation=self.recommendation,
				event_type=AuditEvent.EventType.REVIEW_APPROVED,
			).exists()
		)

	def test_model_rejects_final_decision_without_acknowledgements(self):
		review = ClinicalReview(
			recommendation=self.recommendation,
			reviewer=self.user,
			decision=ClinicalReview.Decision.APPROVED,
		)

		with self.assertRaises(ValidationError) as raised:
			review.full_clean()

		self.assertIn('limitations_acknowledged', raised.exception.message_dict)
		self.assertIn('missing_data_acknowledged', raised.exception.message_dict)

	def test_model_rejects_override_without_reason(self):
		review = ClinicalReview(
			recommendation=self.recommendation,
			reviewer=self.user,
			decision=ClinicalReview.Decision.OVERRIDDEN,
			limitations_acknowledged=True,
			missing_data_acknowledged=True,
		)

		with self.assertRaises(ValidationError) as raised:
			review.full_clean()

		self.assertIn('override_reason', raised.exception.message_dict)

	def test_recommendation_admin_governance_fields_are_read_only(self):
		model_admin = TreatmentRecommendationAdmin(TreatmentRecommendation, admin.site)

		self.assertIn('status', model_admin.readonly_fields)
		self.assertIn('confidence_level', model_admin.readonly_fields)
		self.assertIn('risk_level', model_admin.readonly_fields)
		self.assertIn('clinician_review_required', model_admin.readonly_fields)
		self.assertIn('generated_by', model_admin.readonly_fields)
		self.assertIn('model_version', model_admin.readonly_fields)
