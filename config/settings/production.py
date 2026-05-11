from .base import *  # noqa: F403,F401

DEBUG = False

if SECRET_KEY == 'django-insecure-change-me-before-production':
	raise RuntimeError('Production requires a non-default DJANGO_SECRET_KEY.')

if not ALLOWED_HOSTS:
	raise RuntimeError('Production requires DJANGO_ALLOWED_HOSTS to be configured.')