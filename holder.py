from celery import Celery

celery = Celery('celery_example', include=['strings.reverse'])
