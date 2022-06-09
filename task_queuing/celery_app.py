""" Celery queue broker configuration. """
import celery
import task_queuing.consumers as consumers
import os

# `.env` file for the RABBITMQ_USERNAME and RABBITMQ_PASSWORD
from dotenv import load_dotenv

queue_broker = celery.Celery("__name__")

load_dotenv(verbose=True)
RABBITMQ_USERNAME = os.getenv("RABBITMQ_USERNAME")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD")

# Configure the Celery task broker, to use RabbitMQ with Redis to store the results.
queue_broker.conf.update(
    broker_url=[
        f"amqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@10.128.93.11:5672//",
        f"amqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@10.128.93.12:5672//",
        f"amqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@10.128.93.13:5672//",
        f"amqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@10.128.93.14:5672/the_vhost",
        f"amqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@10.128.93.15:5672/the_vhost",
    ],
    worker_prefetch_multiplier="1",
    result_backend="redis://localhost:6379/1",
    task_serializer="json",
    accept_content=["json", "pickle"],
    imports=(
        "task_queuing.task_logging",
        "task_queuing.tasks.number",
        "task_queuing.tasks.text",
        "task_queuing.tasks.custom",
        "task_queuing.tasks.environment",
    ),
    task_create_missing_queues=True,
    task_routes={
        "task_queuing.tasks.text.*": {"queue": "zengenti.cloud.text_queue"},
        "task_queuing.tasks.number.*": {"queue": "zengenti.cloud.number_queue"},
        "task_queuing.tasks.environment.*": {"queue": "environment_queue"},
    },
)

# Add the custom consumers, which don't use standard Celery format messages.
queue_broker.steps["consumer"].add(consumers.SubstitutionCypher)

# make_capitals = celery.Celery.tasks.add[custom_text.Capitalize]
