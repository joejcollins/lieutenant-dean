""" Celery text manipulations. """
import time
from task_queue.celery_app import queue
import info_module.text as text


@queue.task(bind=True, name='text.slowly_reverse_string')
def slowly_reverse_string(self, string_to_reverse):
    """ Reverse the string but take 10 seconds to do it. """
    counter = 10
    for i in range(0, counter):
        self.update_state(state='PROGRESS', meta={'done': i, 'total': counter})
        time.sleep(1)
    return text.reverse_string(string_to_reverse)
