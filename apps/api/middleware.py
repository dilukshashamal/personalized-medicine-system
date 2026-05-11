import uuid

from config.logging import correlation_id_var


class CorrelationIdMiddleware:
	HEADER_NAME = 'HTTP_X_CORRELATION_ID'
	RESPONSE_HEADER = 'X-Correlation-ID'

	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		correlation_id = request.META.get(self.HEADER_NAME) or str(uuid.uuid4())
		token = correlation_id_var.set(correlation_id)
		request.correlation_id = correlation_id
		try:
			response = self.get_response(request)
		finally:
			correlation_id_var.reset(token)

		response[self.RESPONSE_HEADER] = correlation_id
		return response