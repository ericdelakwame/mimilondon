from __future__ import absolute_import, unicode_literals
from django.conf import settings
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mimilondon.settings')

app = Celery('mimilondon')

app.config_from_object('django.conf:settings', namespace='Celery')

app.autodiscover_tasks()


