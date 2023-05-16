""" Celery arithmetic. """
import time

import pkg_captain_black.numbers as numbers
from celery_redis.main import APP


@APP.task(bind=True)
def slowly_add_two_numbers(self, first_number: int, second_number: int) -> int:
    """Add the numbers but take 10 seconds to do it."""
    counter = 10
    for i in range(counter):
        self.update_state(state="PROGRESS", meta={"done": i, "total": counter})
        time.sleep(1)
    return numbers.add_two_numbers(first_number, second_number)
