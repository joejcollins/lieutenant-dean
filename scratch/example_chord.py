"""A chord is a task that only executes after all of the tasks in a group have finished executing.  This seems
like strange use of the term 'chord' to me.  Typically chord is notes that are played together, but that is a
group in Celery parlance.
"""
import celery
import celery_queue_rabbit.tasks.text as text_tasks

text_task_group = []
text_task_group.append(text_tasks.slowly_reverse_string.s("qwerty"))
text_task_group.append(text_tasks.slowly_reverse_string.s("asdfgh"))
text_task_group.append(text_tasks.slowly_reverse_string.s("zxcvbn"))

# The chord passes the result of the group so use `si`
# (an immutable signature) so the result is ignored.
chord_task = text_tasks.slowly_reverse_string.si("eat my shorts")

chord_result = celery.chord(text_task_group, chord_task)()
