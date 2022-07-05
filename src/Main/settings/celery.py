import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Main.settings')

CLERY_BROKER_URL = 'amqp://'+ os.getenv('RABBITMQ_USER') +':' + os.getenv('RABBITMQ_PASSWORD') +'@'+ os.getenv('RABBITMQ_HOST') + ':'+ os.getenv('RABBITMQ_PORT')

app = Celery('DJANGO-DEMO', broker = CLERY_BROKER_URL)

app.conf.task_default_queue = "demo-queue"


# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')





# Load task modules from all registered Django apps.
app.autodiscover_tasks()