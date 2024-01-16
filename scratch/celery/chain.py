"""Tasks running in order with one task using the output of another task.

The tasks are given a UUID so the log can be viewed during the run.
"""
import celery
import celery_queue_rabbit.tasks.text as text_tasks

# .si = Signature Immutable (i.e. the task doesn't need the output of the previous task)
reverse_it = text_tasks.slowly_reverse_string.si("qwerty")
reverse_it.id = celery.uuid()
# .s = Signature mutable (i.e. the task takes the output of the previous task)
reverse_it_back = text_tasks.slowly_reverse_string.s()
reverse_it_back.id = celery.uuid()

result = celery.chain(reverse_it, reverse_it_back)()
print(f"Chain of {reverse_it.id} and {reverse_it_back.id} now on the broker.")
