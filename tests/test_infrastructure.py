from django.test import SimpleTestCase, override_settings
from rest_framework.test import APIRequestFactory

from apps.api.health import get_health_status
from apps.api.middleware import CorrelationIdMiddleware


class HealthStatusTests(SimpleTestCase):
	@override_settings(ENVIRONMENT='production', CELERY_TASK_ALWAYS_EAGER=True)
	def test_health_status_contains_environment_and_celery_details(self):
		status = get_health_status()

		self.assertEqual(status['environment'], 'production')
		self.assertTrue(status['celery']['task_always_eager'])


class CorrelationIdMiddlewareTests(SimpleTestCase):
	def test_middleware_sets_response_header(self):
		factory = APIRequestFactory()
		request = factory.get('/api/v1/health/')

		def get_response(incoming_request):
			from django.http import JsonResponse

			return JsonResponse({'ok': True, 'correlation_id': incoming_request.correlation_id})

		middleware = CorrelationIdMiddleware(get_response)
		response = middleware(request)

		self.assertIn('X-Correlation-ID', response)
		self.assertEqual(response['X-Correlation-ID'], request.correlation_id)