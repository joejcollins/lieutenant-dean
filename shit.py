""" Scratch pad. """
from task_queue.text import slowly_reverse_string

import celery

tasks = []
tasks.append(slowly_reverse_string.s("qwerty"))
tasks.append(slowly_reverse_string.s("asdfgh"))
tasks.append(slowly_reverse_string.s("zxcvbn"))

# The chord passes the result of the group so use `si`
# (an immutable signature) so the result is ignored.
final_task = slowly_reverse_string.si("eat my shorts")

chain_of_tasks = celery.chord(tasks, final_task)()
