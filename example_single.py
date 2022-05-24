""" Scratch pad. """
from task_queues.text import slowly_reverse_string

task = slowly_reverse_string.si("shit")

result = task.delay()
print("Single task on the queue.")
