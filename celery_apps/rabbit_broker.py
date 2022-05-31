""" Rabbit queue broker configuration. """
import celery
import rabbit_tasks.text as text_tasks

rabbit_queues = celery.Celery("__name__")

rabbit_queues.conf.update(
    broker_url="amqp://the_user:the_password@localhost:5672/the_vhost",
    worker_prefetch_multiplier="1",
    result_backend="rpc://",
    task_serializer="json",
    accept_content=["json", "pickle"],
    imports=("celery_apps.task_logging", "celery_apps.rabbit_tasks.text"),
    task_create_missing_queues=True,
    task_routes={
        "celery_apps.rabbit_tasks.text.*": {"queue": "text_queue"},
    },
)


rabbit_queues.steps["consumer"].add(text_tasks.SubstitutionCypher)
