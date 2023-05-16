""" Celery queue broker configuration. """
import celery
import celery_queue_rabbit.consumers as consumers
import logging

queue_broker = celery.Celery("__name__")

# Configure the Celery task broker, to use RabbitMQ with Redis to store the results.
queue_broker.conf.update(
    broker_url="amqp://the_user:the_password@localhost:5672/the_vhost",
    worker_prefetch_multiplier="1",
    result_backend="redis://localhost:6379/1",
    task_serializer="json",
    accept_content=["json", "pickle"],
    imports=(
        "celery_queue_rabbit.task_logging",
        "celery_queue_rabbit.tasks.number",
        "celery_queue_rabbit.tasks.text",
        "celery_queue_rabbit.tasks.custom",
        "celery_queue_rabbit.tasks.ansible",
    ),
    task_create_missing_queues=True,
    task_routes={
        "celery_queue_rabbit.tasks.ansible.*": {"queue": "ansible_queue"},
        "celery_queue_rabbit.tasks.text.*": {"queue": "text_queue"},
        "celery_queue_rabbit.tasks.number.*": {"queue": "number_queue"},
    },
    worker_hijack_root_logger=False,
)

# logger = logging.getLogger()

# # StreamHandler
# sh = logging.StreamHandler()
# logger.addHandler(sh)

# Add the custom consumers, which don't use standard Celery format messages.
queue_broker.steps["consumer"].add(consumers.SubstitutionCypher)

# make_capitals = celery.Celery.tasks.add[custom_text.Capitalize]
