""" Celery text manipulations. """
import logging
import time

import info_module.text as text
from celery.signals import task_postrun, task_prerun

from task_queue.celery_app import queue

# Attempt to set up logger as per
# https://stackoverflow.com/questions/25281612/celery-log-each-task-run-to-its-own-file


@queue.task(bind=True, name='text.slowly_reverse_string')
def slowly_reverse_string(self, string_to_reverse):
    """ Reverse the string but take 10 seconds to do it. """
    logger = logging.getLogger(self.request.id)
    logger.info(f'Reversing {string_to_reverse}.')
    counter = 10
    for i in range(0, counter):
        self.update_state(state='PROGRESS', meta={'done': i, 'total': counter})
        logger.info(f'Reversing stage {i} of counter.')
        time.sleep(1)
    return text.reverse_string(string_to_reverse)


@task_prerun.connect
def prepare_logging(sender=None, task_id=None, task=None, *args, **kwargs):
    """Log each task to a separate file."""
    import debugpy
    debugpy.listen(('0.0.0.0', 8080))
    debugpy.wait_for_client()
    debugpy.breakpoint()
    logger = logging.getLogger(task_id)
    # optionally logging on the Console as well as file
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.INFO)
    # Adding File Handle with file path. Filename is task_id
    task_handler = logging.FileHandler(f'../logs/{task_id}.log')
    task_handler.setLevel(logging.INFO)
    # Add the handlers
    logger.addHandler(task_handler)
    logger.addHandler(stream_handler)


@task_postrun.connect
def close_logging(sender=None, task_id=None, task=None, retval=None, state=None, *args, **kwargs):
    # getting the same logger and closing all handles associated with it
    logger = logging.getLogger(task_id)
    logger.info('closing files')
    for handler in logger.handlers:
        handler.flush()
        handler.close()
    logger.handlers = []

