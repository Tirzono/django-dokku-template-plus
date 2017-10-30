web: gunicorn --pythonpath {{ project_name }} {{ project_name }}.wsgi
worker: sh dokku/celery_worker.sh
