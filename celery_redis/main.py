"""Run the Celery app."""
from celery import Celery

# # Get the worker name from the environment variable
# WORKER = os.environ.get("CELERY_CONFIG", "default")

# Create a Celery app
APP = Celery(__name__)

# Configure the Celery task broker, with default settings.
APP.conf.update(
    broker_url="redis://localhost:6379/0",
    worker_prefetch_multiplier="1",
    result_backend="redis://localhost:6379/1",
    task_serializer="json",
    accept_content=["json", "pickle"],
    imports=(
        "celery_redis.tasks.numbers",
        "celery_redis.tasks.text",
    ),
    task_create_missing_queues=True,
)
