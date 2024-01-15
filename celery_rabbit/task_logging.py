import logging

from celery.signals import setup_logging, task_postrun, task_prerun

# Attempt to set up logger as per the example at:
# https://stackoverflow.com/questions/25281612/celery-log-each-task-run-to-its-own-file
# I could not get the decorator `@task_prerun.connect(sender='slowly_reverse_string', weak=False)` to work so
# the selection of which tasks to log is made with a conditional statement in the @task_prerun.connect.


@task_prerun.connect
def prepare_logging(sender=None, task_id=None, **kwargs):
    """Log each task to a separate file."""
    # Set the global collection level to debug so the info message can get through, setting the level
    # individually on the handlers does not seem to work.  I must be missing something.
    logging.basicConfig(level=logging.INFO)
    # Get a logger based on the unique name of the task.
    logger = logging.getLogger(task_id)
    # logger.propagate = False
    # Logging to the console.
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter("[%(asctime)s][%(levelname)s] %(message)s")
    stream_handler.setFormatter(formatter)
    # @task_prerun.connect(sender='slowly_reverse_string', weak=False) did not work for me (but YMMV) so
    # add the file log for some tasks based on the name of the task.
    if sender.__name__ == "run_playbook":
        # Adding File Handle with where the filename is task_id.
        task_handler = logging.FileHandler(
            f"/workspace/captain-black/logs/playbook_output/{task_id}.log", mode="a+", encoding="ascii"
        )
        logger.addHandler(task_handler)
    logger.addHandler(stream_handler)


@task_postrun.connect
def close_logging(sender=None, task_id=None, **kwargs):
    """Close the task logger, even if it wasn't opened."""
    logger = logging.getLogger(task_id)
    for handler in logger.handlers:
        handler.flush()
        handler.close()


@setup_logging.connect
def setup_celery_logging(**kwargs):
    """Completely disable the Celery logging.  Celery messes with the root logger
    so the LoggingProxy has no fileno which causes ansible-runner to fail.
    """
    pass
