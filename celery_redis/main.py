""" """
import os
import sys
import logging
from celery import Celery
from celery.utils.log import get_task_logger
from celery.signals import after_setup_logger

# Get the worker name from the environment variable
WORKER = os.environ.get("CELERY_CONFIG", "default")

# Create a Celery app
APP = Celery(__name__)

# Configure the Celery task broker, with default settings.
APP.conf.update(
    broker_url="redis://localhost:6379/0",
    worker_prefetch_multiplier="1",
    result_backend="redis://localhost:6379/1",
    task_serializer="json",
    accept_content=["json", "pickle"],
    imports=(
        "celery_redis.tasks.numbers",
        "celery_redis.tasks.text",
    ),
    task_create_missing_queues=True,
    task_routes={
        "celery_queue_rabbit.tasks.text.*": {"queue": "text_queue"},
        "celery_queue_rabbit.tasks.numbers.*": {"queue": "number_queue"},
    },
    worker_hijack_root_logger=False,
)

# Configure additional Celery
APP.config_from_object(f"{WORKER}_config")

# Create a logger for your tasks
logger = get_task_logger(__name__)

# Create a separate logger for error logs
error_logger = logging.getLogger("error_logger")
error_logger.setLevel(logging.ERROR)

# Create a FileHandler for error logs
error_log_file = APP.conf.task_error_log_file
error_handler = logging.FileHandler(error_log_file)
error_formatter = logging.Formatter(APP.conf.task_error_log_format)
error_handler.setFormatter(error_formatter)
error_logger.addHandler(error_handler)


@after_setup_logger.connect()
def logger_setup_handler(logger, **kwargs) -> None:
    """ Control where stdout goes. """
    my_handler = logging.StreamHandler(sys.stdout)
    my_handler.setLevel(logging.DEBUG)
    my_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )  # custom formatter
    my_handler.setFormatter(my_formatter)
    logger.addHandler(my_handler)

    logging.info("My log handler connected -> Global Logging")
