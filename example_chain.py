""" Scratch pad. """
import celery

from celery_apps.redis_tasks.numbers import slowly_add_two_numbers
from celery_apps.redis_tasks.text import slowly_reverse_string

# .si = Signature Immutable (i.e. the task doesn't need the output of the previous task)
task1 = slowly_reverse_string.si("qwerty")
# .s = Signature mutable (i.e. the task takes the output of the previous task)
task2 = slowly_reverse_string.s()
task3 = slowly_add_two_numbers.si(1, 2)
task4 = slowly_add_two_numbers.si(3, 4)

result = celery.chain(task1, task2, task3, task4)()
print("Chain of tasks now on the Redis broker.")
