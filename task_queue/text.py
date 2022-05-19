""" Celery text manipulations. """
import logging
import time

import info_module.text as text
from celery.signals import task_postrun, task_prerun

from task_queue.celery_app import queue

TASK_WITH_LOGGING = ['text.slowly_reverse_string']


@task_prerun.connect(sender=TASK_WITH_LOGGING)
def prepare_logging(signal=None, sender=None, task_id=None, task=None, args=None, **kwargs):
    """ File handler """
    logger = logging.getLogger(task_id)
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')
    # optionally logging on the Console as well as file
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.INFO)
    # Adding File Handle with file path. Filename is task_id
    task_handler = logging.FileHandler('/workspace/captain-black/tmp/shit.log')
    task_handler.setFormatter(formatter)
    task_handler.setLevel(logging.INFO)
    # Add the handlers
    # logger.addHandler(task_handler)
    # logger.addHandler(stream_handler)


@task_postrun.connect(sender=TASK_WITH_LOGGING)
def close_logging(signal=None, sender=None, task_id=None, task=None, args=None, retval=None, state=None, **kwargs):
    # getting the same logger and closing all handles associated with it
    logger = logging.getLogger(task_id)
    for handler in logger.handlers:
        handler.flush()
        handler.close()
    logger.handlers = []

# @app.task(base=CallbackTask, bind=True)
# def calc(self, syntax):
#     # getting logger with name Task ID. This is already
#     # created and setup in prepare_logging
#     logger = logging.getLogger(self.request.id)
#     some_func()
#     logger.info('started')


@queue.task(bind=True, name='text.slowly_reverse_string')
def slowly_reverse_string(self, string_to_reverse):
    """ Reverse the string but take 10 seconds to do it. """
    logger = logging.getLogger(self.request.id)
    import debugpy
    debugpy.listen(('0.0.0.0', 8080))
    debugpy.wait_for_client()
    debugpy.breakpoint()
    logger.info(f'Reversing {string_to_reverse}.')
    counter = 10
    for i in range(0, counter):
        self.update_state(state='PROGRESS', meta={'done': i, 'total': counter})
        logger.info(f'Reversing stage {i} of counter.')
        time.sleep(1)
    return text.reverse_string(string_to_reverse)
