""" Celery configuration. """
import celery

queue = celery.Celery("__name__")

queue.conf.update(
    broker_url="redis://localhost:6379/1",
    worker_prefetch_multiplier="1",
    result_backend="redis://localhost:6379/1",
    task_serializer="json",
    accept_content=["json", "pickle"],
    imports=('task_queue.text', 'task_queue.numbers'),
    task_create_missing_queues=True,
    task_routes={
        "task_queue.text.*": {"queue": "text_queue"},
        "task_queue.numbers.*": {"queue": "numbers_queue"},
    },
)
