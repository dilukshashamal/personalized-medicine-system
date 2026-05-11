from .base import *  # noqa: F403,F401

DEBUG = False

if SECRET_KEY == 'django-insecure-change-me-before-production':
	raise RuntimeError('Production requires a non-default DJANGO_SECRET_KEY.')

if not ALLOWED_HOSTS:
	raise RuntimeError('Production requires DJANGO_ALLOWED_HOSTS to be configured.')

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = int(get_env('DJANGO_SECURE_HSTS_SECONDS', '31536000'))
SECURE_HSTS_INCLUDE_SUBDOMAINS = get_bool_env('DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS', True)
SECURE_HSTS_PRELOAD = get_bool_env('DJANGO_SECURE_HSTS_PRELOAD', True)
SECURE_REFERRER_POLICY = get_env('DJANGO_SECURE_REFERRER_POLICY', 'same-origin')
