"""Send a single task to the queue."""
import celery_queue_rabbit.tasks.environment as environment_tasks

task = environment_tasks.delete_environment.si("an_alias")

result = task.delay()

print("Delete alias on queue.")
