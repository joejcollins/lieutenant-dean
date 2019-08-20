import os
from celery import Celery

app = Celery(__name__)
app.conf.update({
    'broker_url': "redis://localhost:6379/0",
    'result_backend': "redis://localhost:6379/0",
    'imports': (
        'tasks',
    ),
    'task_serializer': 'json',
    'result_serializer': 'json',
    'accept_content': ['json']})