""" Rabbit queue broker configuration. """
import celery

redis_queue = celery.Celery("__name__")

redis_queue.conf.update(
    broker_url = 'amqp://myuser:mypassword@localhost:5672/myvhost',
    worker_prefetch_multiplier="1",
    result_backend="redis://localhost:6379/1",
    task_serializer="json",
    accept_content=["json", "pickle"],
    imports=("task_queues.task_logging", "task_queues.redis_tasks.text", "task_queues.redis_tasks.numbers"),
    task_create_missing_queues=True,
    task_routes={
        "task_queues.text.*": {"queue": "text_queue"},
        "task_queues.numbers.*": {"queue": "numbers_queue"},
    },
)


