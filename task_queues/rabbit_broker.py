""" Rabbit queue broker configuration. """
import celery

rabbit_queues = celery.Celery("__name__")

rabbit_queues.conf.update(
    broker_url="amqp://the_user:the_password@localhost:5672/the_vhost",
    worker_prefetch_multiplier="1",
    result_backend="rpc://",
    task_serializer="json",
    accept_content=["json", "pickle"],
    imports=("task_queues.task_logging", "task_queues.rabbit_tasks.text"),
    task_create_missing_queues=True,
    task_routes={
        "task_queues.rabbit_tasks.text.*": {"queue": "text_queue"},
    },
)
