from django.contrib import admin

from .models import PatientProfile


@admin.action(description='Mark selected patients as active')
def mark_patients_active(modeladmin, request, queryset):
	queryset.update(record_status=PatientProfile.RecordStatus.ACTIVE)


@admin.action(description='Archive selected patients')
def archive_patients(modeladmin, request, queryset):
	queryset.update(record_status=PatientProfile.RecordStatus.ARCHIVED)


@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
	list_display = (
		'external_id',
		'record_status',
		'consent_status',
		'sex_at_birth',
		'date_of_birth',
		'updated_at',
	)
	list_filter = ('record_status', 'consent_status', 'sex_at_birth', 'updated_at')
	search_fields = ('external_id', 'clinical_notes_summary')
	readonly_fields = ('id', 'created_at', 'updated_at')
	ordering = ('-updated_at',)
	date_hierarchy = 'updated_at'
	list_per_page = 30
	actions = (mark_patients_active, archive_patients)
	fieldsets = (
		('Identity', {'fields': ('id', 'external_id', 'record_status', 'consent_status')}),
		('Clinical Profile', {'fields': ('date_of_birth', 'sex_at_birth', 'clinical_notes_summary')}),
		(
			'Structured Medical Context',
			{
				'fields': (
					'diagnoses',
					'comorbidities',
					'medications',
					'allergies',
					'lifestyle_factors',
					'disease_progression_summary',
				)
			},
		),
		('Audit Timestamps', {'fields': ('created_at', 'updated_at')}),
	)
