""" Celery arithmetic. """
import time

import info_module.numbers as numbers
import task_queuing.celery_app as app


@app.queue_broker.task(bind=True, name="number.slowly_add_two_numbers")
def slowly_add_two_numbers(self, first_number, second_number):
    """Add the numbers but take 10 seconds to do it."""
    counter = 10
    for i in range(0, counter):
        self.update_state(state="PROGRESS", meta={"done": i, "total": counter})
        time.sleep(1)
    return numbers.add_two_numbers(first_number, second_number)
