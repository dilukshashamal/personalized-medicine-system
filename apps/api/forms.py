from django import forms

from apps.genomics.models import GenomicInsight
from apps.patients.models import PatientProfile


class RecommendationWorkspaceForm(forms.Form):
	FULL_WIDTH_FIELDS = {
		'diagnoses',
		'medications',
		'allergies',
		'clinical_notes_summary',
		'evidence_summary',
	}

	external_id = forms.CharField(
		label='Patient ID',
		max_length=100,
		widget=forms.TextInput(attrs={'placeholder': 'Example: HX-2048'}),
	)
	date_of_birth = forms.DateField(
		label='Date of birth',
		required=False,
		widget=forms.DateInput(attrs={'type': 'date'}),
	)
	sex_at_birth = forms.ChoiceField(
		label='Sex at birth',
		choices=PatientProfile.SexAtBirth.choices,
		required=False,
	)
	consent_status = forms.CharField(
		label='Consent status',
		max_length=50,
		initial='pending_review',
		widget=forms.TextInput(attrs={'placeholder': 'pending_review'}),
	)
	diagnoses = forms.CharField(
		label='Diagnoses',
		required=False,
		widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'One diagnosis per line'}),
	)
	medications = forms.CharField(
		label='Current medications',
		required=False,
		widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'One medication per line'}),
	)
	allergies = forms.CharField(
		label='Allergies and sensitivities',
		required=False,
		widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'One allergy or sensitivity per line'}),
	)
	clinical_notes_summary = forms.CharField(
		label='Clinical notes summary',
		required=False,
		widget=forms.Textarea(
			attrs={'rows': 4, 'placeholder': 'Relevant history, progression, prior response, and care constraints'}
		),
	)
	gene_symbol = forms.CharField(
		label='Gene',
		required=False,
		max_length=50,
		widget=forms.TextInput(attrs={'placeholder': 'Example: EGFR'}),
	)
	variant = forms.CharField(
		label='Variant',
		required=False,
		max_length=255,
		widget=forms.TextInput(attrs={'placeholder': 'Example: L858R'}),
	)
	clinical_significance = forms.ChoiceField(
		label='Clinical significance',
		choices=[('', '---------'), *GenomicInsight.Significance.choices],
		required=False,
	)
	is_actionable = forms.BooleanField(label='Actionable finding', required=False)
	evidence_summary = forms.CharField(
		label='Evidence summary',
		required=False,
		widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Source, relevance, and confidence notes'}),
	)

	def _split_lines(self, value: str) -> list[str]:
		return [line.strip() for line in value.splitlines() if line.strip()]

	def get_patient_payload(self) -> dict:
		cleaned = self.cleaned_data
		return {
			'external_id': cleaned['external_id'],
			'date_of_birth': cleaned.get('date_of_birth'),
			'sex_at_birth': cleaned.get('sex_at_birth') or PatientProfile.SexAtBirth.UNKNOWN,
			'consent_status': cleaned['consent_status'],
			'diagnoses': self._split_lines(cleaned.get('diagnoses', '')),
			'medications': self._split_lines(cleaned.get('medications', '')),
			'allergies': self._split_lines(cleaned.get('allergies', '')),
			'clinical_notes_summary': cleaned.get('clinical_notes_summary', ''),
		}

	def get_genomic_payload(self) -> dict | None:
		cleaned = self.cleaned_data
		if not cleaned.get('gene_symbol') and not cleaned.get('variant'):
			return None

		return {
			'gene_symbol': cleaned.get('gene_symbol', ''),
			'variant': cleaned.get('variant', ''),
			'clinical_significance': cleaned.get('clinical_significance') or GenomicInsight.Significance.UNCERTAIN,
			'is_actionable': cleaned.get('is_actionable', False),
			'evidence_summary': cleaned.get('evidence_summary', ''),
		}
