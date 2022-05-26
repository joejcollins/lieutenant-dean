""" Celery arithmetic. """
import logging
import time

import info_module.numbers as numbers

from celery_apps.redis_broker import redis_queues


@redis_queues.task(bind=True)
def slowly_add_two_numbers(self, first_number, second_number):
    """ Add the numbers but take 10 seconds to do it. """
    logger = logging.getLogger(self.request.id)
    counter = 10
    for i in range(0, counter):
        self.update_state(state='PROGRESS', meta={'done': i, 'total': counter})
        logger.info(f'Adding stage {i} of counter.')
        time.sleep(1)
    return numbers.add_two_numbers(first_number, second_number)
