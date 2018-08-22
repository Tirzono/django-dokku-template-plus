import os
from distutils.util import strtobool

from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

INTERNAL_IPS = ('127.0.0.1', )


if DEBUG and not IS_CELERY_ENVIRONMENT:
    INSTALLED_APPS = INSTALLED_APPS + [
        'debug_toolbar',
    ]

    MIDDLEWARE = MIDDLEWARE + [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    if strtobool(os.environ.get('DOCKER_ENV', '0')):
        DEBUG_TOOLBAR_CONFIG = {
            'SHOW_TOOLBAR_CALLBACK': lambda r: True
        }


EMAIL_BACKEND = env('EMAIL_BACKEND', default='django.core.mail.backends.dummy.EmailBackend')
EMAIL_BACKEND_ALLOWED = (
    'django.core.mail.backends.console.EmailBackend',
    'django.core.mail.backends.dummy.EmailBackend',
    'utils.mail.backends.mailhog.EmailBackend'
)

EMAIL_BACKEND_MAILHOG_HOST = env('EMAIL_BACKEND_MAILHOG_HOST', default='127.0.0.1')
EMAIL_BACKEND_MAILHOG_PORT = env('EMAIL_BACKEND_MAILHOG_PORT', default='1025')
