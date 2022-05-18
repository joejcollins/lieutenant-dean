""" Scratch pad. """
from task_queue.text import slowly_reverse_string
from task_queue.numbers import slowly_add_two_numbers

import celery

task1 = slowly_reverse_string.s("qwerty")
task2 = slowly_reverse_string.si("asdfgh")
task3 = slowly_add_two_numbers.si(1, 2)
task4 = slowly_add_two_numbers.si(3, 4)

res = celery.chain(task1, task3, task2, task4)()
print("Chain on of tasks now on the queue.")
