# ruff: noqa: E501
from .base import *  # noqa: F403
from .base import INSTALLED_APPS
from .base import MIDDLEWARE
from .base import REDIS_URL
from .base import env

from config.utils import is_docker

from csp.constants import NONE, SELF

# GENERAL
# ------------------------------------------------------------------------------
DEBUG = True
SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='!!!SET DJANGO_SECRET_KEY!!!',
)
ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']

# CACHES
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': REDIS_URL,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            # Mimicking memcache behavior.
            # https://github.com/jazzband/django-redis#memcached-exceptions-behavior
            'IGNORE_EXCEPTIONS': True,
        },
    },
}

# EMAIL
# ------------------------------------------------------------------------------
EMAIL_HOST = env('EMAIL_HOST', default='localhost')
EMAIL_PORT = 1025
EMAIL_BACKEND = env(
    'DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend',
)

# WhiteNoise
# ------------------------------------------------------------------------------
INSTALLED_APPS = ['whitenoise.runserver_nostatic', *INSTALLED_APPS]

# django-debug-toolbar
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
        # Disable profiling panel due to an issue with Python 3.12:
        # https://github.com/jazzband/django-debug-toolbar/issues/1875
        'debug_toolbar.panels.profiling.ProfilingPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}
INTERNAL_IPS = ['127.0.0.1', '10.0.2.2']

if is_docker():
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += ['.'.join(ip.split('.')[:-1] + ['1']) for ip in ips]

# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['django_extensions']

# Celery
# ------------------------------------------------------------------------------
if not is_docker():
    CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

# django-zeal
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['django_zeal']
MIDDLEWARE += ['zeal.middleware.zeal_middleware']

# django-csp
# ------------------------------------------------------------------------------
CONTENT_SECURITY_POLICY = {}

CONTENT_SECURITY_POLICY_REPORT_ONLY = {
    'EXCLUDE_URL_PREFIXES': [''],
    'DIRECTIVES': {
        'default-src': [NONE],
        'connect-src': [SELF],
        'img-src': [SELF],
        'form-action': [SELF],
        'frame-ancestors': [SELF],
        'script-src': [SELF, UNSAFE_EVAL],
        'style-src': [SELF],
        'upgrade-insecure-requests': env('DJANGO_CSP_UPGRADE_INSECURE_REQUESTS', default=True),
        # 'report-uri': '/csp-report/',
    },
}

# django-browser-reload
# ------------------------------------------------------------------------------
INSTALLED_APPS += 'django_browser_reload'
MIDDLEWARE += ['django_browser_reload.middleware.BrowserReloadMiddleware']

# Project Specific Settings
# ------------------------------------------------------------------------------
