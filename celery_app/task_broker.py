""" Rabbit queue broker configuration. """
import celery
import celery_app.tasks.custom_text as custom_text

broker_config = celery.Celery("__name__")

broker_config.conf.update(
    broker_url="amqp://the_user:the_password@localhost:5672/the_vhost",
    worker_prefetch_multiplier="1",
    result_backend="redis://localhost:6379/1",
    task_serializer="json",
    accept_content=["json", "pickle"],
    imports=("celery_app.task_logging", "celery_app.tasks.custom_text"),
    task_create_missing_queues=True,
    task_routes={
        "celery_apps.rabbit_tasks.text.*": {"queue": "text_queue"},
    },
)

broker_config.steps["make_secret"].add(custom_text.SubstitutionCypher)
