""" Scratch pad. """
from task_queue.text import slowly_reverse_string
from task_queue.numbers import slowly_add_two_numbers

import celery

task1 = slowly_reverse_string.s("qwerty")
task2 = slowly_reverse_string.si("asdfgh")
task3 = slowly_reverse_string.si("zxcvbn")

res = celery.chain(task1, task2, task3)()
