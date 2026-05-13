import uuid

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class ClinicalReview(models.Model):
	class Decision(models.TextChoices):
		NEEDS_REVIEW = 'needs_review', 'Needs Review'
		APPROVED = 'approved', 'Approved'
		OVERRIDDEN = 'overridden', 'Overridden'
		REJECTED = 'rejected', 'Rejected'

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	recommendation = models.OneToOneField(
		'recommendations.TreatmentRecommendation',
		on_delete=models.CASCADE,
		related_name='clinical_review',
	)
	reviewer = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.SET_NULL,
		blank=True,
		null=True,
		related_name='clinical_reviews',
	)
	decision = models.CharField(
		max_length=20,
		choices=Decision.choices,
		default=Decision.NEEDS_REVIEW,
	)
	review_notes = models.TextField(blank=True)
	override_reason = models.TextField(blank=True)
	limitations_acknowledged = models.BooleanField(default=False)
	missing_data_acknowledged = models.BooleanField(default=False)
	reviewed_at = models.DateTimeField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-updated_at']

	def __str__(self):
		return f'Review for {self.recommendation.title}'

	def clean(self):
		super().clean()
		final_decisions = {
			self.Decision.APPROVED,
			self.Decision.OVERRIDDEN,
			self.Decision.REJECTED,
		}
		errors = {}

		if self.decision == self.Decision.OVERRIDDEN and not self.override_reason:
			errors['override_reason'] = 'Override reason is required when a recommendation is overridden.'

		if self.decision in final_decisions:
			if self.reviewer_id is None:
				errors['reviewer'] = 'Reviewer is required for final review decisions.'
			if not self.limitations_acknowledged:
				errors['limitations_acknowledged'] = 'Reviewer must acknowledge recommendation limitations.'
			if not self.missing_data_acknowledged:
				errors['missing_data_acknowledged'] = 'Reviewer must acknowledge missing data considerations.'

		if errors:
			raise ValidationError(errors)

	def save(self, *args, **kwargs):
		if self.decision != self.Decision.NEEDS_REVIEW and self.reviewed_at is None:
			self.reviewed_at = timezone.now()
		self.full_clean()
		super().save(*args, **kwargs)
