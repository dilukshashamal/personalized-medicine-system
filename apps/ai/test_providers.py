import json
from unittest.mock import patch

from django.test import TestCase

from apps.ai.providers import GeminiRecommendationProvider, get_recommendation_provider
from apps.ai.workflow import run_recommendation_workflow


class GeminiProviderTests(TestCase):
	def test_provider_status_selects_gemini_when_configured(self):
		with patch.dict(
			'os.environ',
			{
				'HELIXORA_AI_PROVIDER': 'gemini',
				'GEMINI_API_KEY': 'test-key',
				'GEMINI_MODEL': 'gemini-test-model',
			},
			clear=False,
		):
			provider = get_recommendation_provider()

		self.assertIsInstance(provider, GeminiRecommendationProvider)
		self.assertEqual(provider.model, 'gemini-test-model')

	def test_gemini_json_extraction_handles_fenced_response(self):
		provider = GeminiRecommendationProvider(api_key='test-key', model='gemini-test-model')
		payload = {
			'summary': 'Summary',
			'rationale': 'Rationale',
			'suggested_options': [],
			'evidence_references': [],
			'uncertainty_notes': '',
			'missing_data_flags': [],
			'contraindication_warnings': [],
		}

		extracted = provider._extract_json_text(f"```json\n{json.dumps(payload)}\n```")

		self.assertEqual(json.loads(extracted), payload)

	def test_workflow_falls_back_when_provider_fails(self):
		class FailingProvider:
			provider_name = 'failing'

			def generate(self, *, patient_payload, genomic_payload=None):
				raise RuntimeError('provider unavailable')

		with patch('apps.ai.workflow.get_recommendation_provider', return_value=FailingProvider()):
			result = run_recommendation_workflow(
				patient_data={
					'external_id': 'P-GEMINI-FALLBACK',
					'consent_status': 'granted',
					'diagnoses': ['Condition A'],
					'medications': ['Medication A'],
					'allergies': ['None known'],
					'clinical_notes_summary': 'Stable presentation.',
				},
				genomic_data={
					'gene_symbol': 'EGFR',
					'variant': 'L858R',
					'clinical_significance': 'high',
					'is_actionable': True,
					'evidence_summary': 'Known actionable alteration.',
				},
			)

		self.assertEqual(result.recommendation.generated_by, 'safe-placeholder-engine')
		self.assertIn('safe placeholder rules were used', result.recommendation.uncertainty_notes)
