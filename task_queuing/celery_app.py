""" Celery queue broker configuration. """
import celery
import task_queuing.consumers as consumers

queue_broker = celery.Celery("__name__")

# Configure the Celery task broker, to use RabbitMQ with Redis to store the results.
queue_broker.conf.update(
    broker_url="amqp://the_user:the_password@localhost:5672/the_vhost",
    worker_prefetch_multiplier="1",
    result_backend="redis://localhost:6379/1",
    task_serializer="json",
    accept_content=["json", "pickle"],
    imports=(
        "task_queuing.task_logging",
        "task_queuing.tasks.number",
        "task_queuing.tasks.text",
        "task_queuing.tasks.custom",
        "task_queuing.tasks.ansible",
    ),
    task_create_missing_queues=True,
    task_routes={
        "task_queuing.tasks.text.*": {"queue": "text_queue"},
        "task_queuing.tasks.number.*": {"queue": "number_queue"},
    },
)

# Add the custom consumers, which don't use standard Celery format messages.
queue_broker.steps["consumer"].add(consumers.SubstitutionCypher)

# make_capitals = celery.Celery.tasks.add[custom_text.Capitalize]
