""" Celery Redis text queue manipulations. """
import logging
import time

import info_module.text as info_module_text

from celery_apps.redis_broker import redis_queues


@redis_queues.task(bind=True)  # `bind=True` ensures that the arguments are passed.
def slowly_reverse_string(self, string_to_reverse):
    """ Reverse the string but take 10 seconds to do it. """
    logger = logging.getLogger(self.request.id)
    logger.info(f'Redis: Reversing {string_to_reverse}.')
    counter = 10
    for i in range(0, counter):
        self.update_state(state='PROGRESS', meta={'done': i, 'total': counter})
        logger.info(f'Redis: Reversing stage {i} of counter.')
        time.sleep(1)
    return info_module_text.reverse_string(string_to_reverse)