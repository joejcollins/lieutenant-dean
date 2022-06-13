""" Celery queue broker configuration. """
import celery
import os

import task_queuing.consumers as consumers
from task_queuing.queues import custom_exchange

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
    ),
    task_create_missing_queues=True,
    task_routes={
        "task_queuing.tasks.text.*": {"exchange": custom_exchange,
                                      "routing_key": "high_load",
                                      },
        "task_queuing.tasks.number.*": {"exchange": custom_exchange,
                                        "routing_key": "low_load",
                                        },
        "task_queuing.tasks.environment.*": {"exchange": custom_exchange,
                                             "routing_key": "low_load",
                                             },
    },
)

# Add the custom consumers, which don't use standard Celery format messages.
queue_broker.steps["consumer"].add(consumers.SubstitutionCypher)

# make_capitals = celery.Celery.tasks.add[custom_text.Capitalize]