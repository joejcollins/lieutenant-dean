import logging
from celery.signals import task_prerun, task_postrun
# Attempt to set up logger as per the example at:
# https://stackoverflow.com/questions/25281612/celery-log-each-task-run-to-its-own-file
# I could not get the decorator `@task_prerun.connect(sender='slowly_reverse_string', weak=False)` to work so
# the selection of which tasks to log is made with a conditional statement in the @task_prerun.connect.


@task_prerun.connect
def prepare_logging(sender=None, task_id=None, **kwargs):
    """Log each task to a separate file."""
    # Get a logger based on the unique name of the task.
    logger = logging.getLogger(task_id)
    logger.propagate = False
    # Logging to the console.
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.INFO)
    # @task_prerun.connect(sender='slowly_reverse_string', weak=False) did not work for my but YMMV so
    # add the file log for some tasks based on the name of the task.
    if sender.__name__ == 'slowly_reverse_string':
        # Adding File Handle with file path. Filename is task_id
        task_handler = logging.FileHandler(f'../logs/{task_id}.log')
        task_handler.setLevel(logging.INFO)
        logger.addHandler(task_handler)
    logger.addHandler(stream_handler)


@task_postrun.connect
def close_logging(sender=None, task_id=None, **kwargs):
    """Close the task logger, even if it wasn't opened."""
    logger = logging.getLogger(task_id)
    for handler in logger.handlers:
        handler.flush()
        handler.close()
    logger.handlers = []
