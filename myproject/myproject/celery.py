import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from django.apps import apps 
import logging


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.config_from_object(settings)

logger = logging.getLogger('celery')

app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])

app.conf.beat_schedule = {
    'reduce-stock-every-10-seconds': {
        'task': 'inventory.tasks.reduce_stock',
        'schedule': crontab(minute='*/1'),  # Runs every minute
    },
}

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')