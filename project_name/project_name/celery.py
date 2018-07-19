from __future__ import absolute_import, unicode_literals

import celery
from django.conf import settings

from {{ project_name }}.settings import set_settings_module


set_settings_module()


class Celery(celery.Celery):
    def on_configure(self):
        import raven
        from raven.contrib.celery import register_logger_signal, register_signal

        client = raven.Client(**settings.RAVEN_CONFIG)

        # register a custom filter to filter out duplicate logs
        register_logger_signal(client)

        # hook into the Celery error handler
        register_signal(client)


app = Celery('{{ project_name }}')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
