""" Celery queue broker configuration. """
import celery
import os

import task_queuing.consumers as consumers
from task_queuing.queues import my_queues

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
        f"amqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@10.128.93.14:5672//",
        f"amqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@10.128.93.15:5672//",
    ],
    # broker="amqp://the_user:the_password@localhost:5672/the_vhost",
    broker_failover_strategy="shuffle",
    worker_prefetch_multiplier="1",
    result_backend="redis://localhost:6379/1",  # rpc:// if running without redis server
    task_serializer="json",
    accept_content=["json", "pickle"],
    imports=(
        "task_queuing.task_logging",
        "task_queuing.tasks.number",
        "task_queuing.tasks.text",
        "task_queuing.tasks.custom",
        "task_queuing.tasks.environment",
        "example_custom_multi_queues",
    ),
    task_create_missing_queues=True,
    task_routes={
        "example_custom_multi_queues.*": {"queue": "zengenti-cloud-low"},
        "task_queuing.tasks.text.*": {"queue": "text_queue"},
        "task_queuing.tasks.number.*": {"queue": "number_queue"},
        "task_queuing.tasks.environment.*": {"queue": "environment_queue"},
    },
)

# Add the custom consumers, which don't use standard Celery format messages.
# queue_broker.steps["consumer"].add(consumers.HighConsumer)
queue_broker.steps["consumer"].add(consumers.LowConsumer)

# make_capitals = celery.Celery.tasks.add[custom_text.Capitalize]
