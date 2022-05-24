""" Scratch pad. """
import celery

from task_queues.rabbit_tasks.text import slowly_reverse_string

# .si = Signature Immutable (i.e. the task doesn't need the output of the previous task)
task1 = slowly_reverse_string.si("qwerty")
# .s = Signature mutable (i.e. the task takes the output of the previous task)
task2 = slowly_reverse_string.s()

result = celery.chain(task1, task2)()
print("Chain of tasks now on the Rabbit broker.")
