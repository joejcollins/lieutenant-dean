"""Send a single task to the queue."""
import task_queuing.tasks.text as text_tasks

task = text_tasks.slowly_reverse_string.si("reverse me")

result = task.delay()

print("Single task on queue.")
