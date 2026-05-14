from rest_framework import mixins, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

from apps.audit.models import AuditEvent
from apps.genomics.models import GenomicInsight
from apps.patients.models import PatientProfile
from apps.recommendations.models import TreatmentRecommendation
from apps.reviews.models import ClinicalReview

from .health import get_operations_health_status, get_public_health_status
from .permissions import IsClinicalApiAuthorized
from .serializers import (
	AuditEventSerializer,
	ClinicalReviewSerializer,
	GenomicInsightSerializer,
	PatientProfileSerializer,
	TreatmentRecommendationSerializer,
)


def _has_clinical_admin_scope(user):
	return bool(
		user
		and user.is_authenticated
		and (user.is_superuser or user.groups.filter(name='clinical_admin').exists())
	)


def _patient_is_accessible_to_user(patient, user):
	if _has_clinical_admin_scope(user):
		return True
	return patient.authorized_users.filter(pk=user.pk).exists()


class PatientScopedViewSetMixin:
	patient_scope_field = ''

	def get_queryset(self):
		queryset = super().get_queryset()
		user = self.request.user
		if _has_clinical_admin_scope(user):
			return queryset
		if self.patient_scope_field:
			return queryset.filter(**{self.patient_scope_field: user}).distinct()
		return queryset.filter(authorized_users=user).distinct()

	def _ensure_patient_access(self, patient):
		if not _patient_is_accessible_to_user(patient, self.request.user):
			raise PermissionDenied('You do not have access to this patient record.')


class HealthCheckView(APIView):
	permission_classes = []
	authentication_classes = []

	def get(self, request):
		return Response(get_public_health_status())


class OperationsHealthCheckView(APIView):
	permission_classes = [IsAdminUser]

	def get(self, request):
		return Response(get_operations_health_status())


class PatientProfileViewSet(PatientScopedViewSetMixin, viewsets.ModelViewSet):
	queryset = PatientProfile.objects.all()
	serializer_class = PatientProfileSerializer
	permission_classes = [IsClinicalApiAuthorized]
	clinical_write_roles = {'clinical_editor', 'clinical_admin'}

	def perform_create(self, serializer):
		patient = serializer.save()
		if not self.request.user.is_superuser:
			patient.authorized_users.add(self.request.user)


class GenomicInsightViewSet(PatientScopedViewSetMixin, viewsets.ModelViewSet):
	queryset = GenomicInsight.objects.select_related('patient').all()
	serializer_class = GenomicInsightSerializer
	permission_classes = [IsClinicalApiAuthorized]
	clinical_write_roles = {'clinical_editor', 'clinical_admin'}
	patient_scope_field = 'patient__authorized_users'

	def perform_create(self, serializer):
		self._ensure_patient_access(serializer.validated_data['patient'])
		serializer.save()

	def perform_update(self, serializer):
		patient = serializer.validated_data.get('patient', serializer.instance.patient)
		self._ensure_patient_access(patient)
		serializer.save()


class TreatmentRecommendationViewSet(PatientScopedViewSetMixin, viewsets.ReadOnlyModelViewSet):
	queryset = TreatmentRecommendation.objects.select_related('patient', 'primary_genomic_insight').all()
	serializer_class = TreatmentRecommendationSerializer
	permission_classes = [IsClinicalApiAuthorized]
	patient_scope_field = 'patient__authorized_users'


class ClinicalReviewViewSet(
	PatientScopedViewSetMixin,
	mixins.ListModelMixin,
	mixins.RetrieveModelMixin,
	mixins.UpdateModelMixin,
	viewsets.GenericViewSet,
):
	queryset = ClinicalReview.objects.select_related('recommendation', 'reviewer').all()
	serializer_class = ClinicalReviewSerializer
	permission_classes = [IsClinicalApiAuthorized]
	clinical_write_roles = {'clinical_reviewer', 'clinical_admin'}
	patient_scope_field = 'recommendation__patient__authorized_users'

	def perform_update(self, serializer):
		self._ensure_patient_access(serializer.instance.recommendation.patient)
		serializer.save(reviewer=self.request.user)


class AuditEventViewSet(PatientScopedViewSetMixin, viewsets.ReadOnlyModelViewSet):
	queryset = AuditEvent.objects.select_related('patient', 'recommendation', 'actor').all()
	serializer_class = AuditEventSerializer
	permission_classes = [IsClinicalApiAuthorized]

	def get_queryset(self):
		queryset = super(PatientScopedViewSetMixin, self).get_queryset()
		user = self.request.user
		if _has_clinical_admin_scope(user):
			return queryset
		return queryset.filter(
			Q(patient__authorized_users=user) | Q(recommendation__patient__authorized_users=user)
		).distinct()
