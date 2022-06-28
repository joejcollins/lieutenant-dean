"""Send a single task to the queue."""
import task_queuing.tasks.ansible as ansible_tasks

# task = text_tasks.slowly_reverse_string.si("reverse me")
# result = task.delay()

task = ansible_tasks.run_playbook.si()
result = task.delay()

print("Ansible task on queue.")
