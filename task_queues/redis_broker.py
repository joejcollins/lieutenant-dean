""" Rabbit queue broker configuration, this broker manages queues on a Redis instance. """
import celery

redis_queues = celery.Celery("__name__")

redis_queues.conf.update(
    broker_url="redis://localhost:6379/1",
    worker_prefetch_multiplier="1",
    result_backend="redis://localhost:6379/1",
    task_serializer="json",
    accept_content=["json", "pickle"],
    imports=("task_queues.task_logging", "task_queues.redis_tasks.text", "task_queues.redis_tasks.numbers"),
    task_create_missing_queues=True,
    task_routes={
        "task_queues.redis_tasks.text.*": {"queue": "text_queue"},
        "task_queues.redis_tasks.numbers.*": {"queue": "numbers_queue"},
    },
)
