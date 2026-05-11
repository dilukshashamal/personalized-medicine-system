import logging
from contextvars import ContextVar


correlation_id_var = ContextVar('correlation_id', default='')


class CorrelationIdFilter(logging.Filter):
	def filter(self, record):
		record.correlation_id = correlation_id_var.get() or 'n/a'
		return True