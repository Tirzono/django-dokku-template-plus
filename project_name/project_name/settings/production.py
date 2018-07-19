from .base import *


RAVEN_CONFIG = {
    'dsn': env('SENTRY_DSN', default=''),
    'environment': 'production',
}

GIT_REV = env('GIT_REV', default=None)

if GIT_REV:
    RAVEN_CONFIG['release'] = GIT_REV

INSTALLED_APPS.append('raven.contrib.django.raven_compat')


CELERY_WORKER_HIJACK_ROOT_LOGGER = False


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'verbose'
        },
        'sentry': {
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'level': 'ERROR'
        },
    },
    'formatters': {
        'verbose': {'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s', }
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False
        },
        'raven': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'sentry.errors': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'celery': {
            'handlers': ['sentry', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

