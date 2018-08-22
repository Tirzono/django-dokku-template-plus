from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

INTERNAL_IPS = ('127.0.0.1', )

MAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND_ALLOWED = ('django.core.mail.backends.console.EmailBackend',)
