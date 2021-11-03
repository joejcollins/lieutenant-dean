""" Scratch pad. """
from task_queue.text import slowly_reverse_string
from task_queue.numbers import slowly_add_two_numbers

import celery

text_tasks = []
text_tasks.append(slowly_reverse_string.s("qwerty"))
text_tasks.append(slowly_reverse_string.s("asdfgh"))
text_tasks.append(slowly_reverse_string.s("zxcvbn"))

# The chord passes the result of the group so use `si`
# (an immutable signature) so the result is ignored.
final_text_task = slowly_reverse_string.si("eat my shorts")

chain_of_text_tasks = celery.chord(text_tasks, final_text_task)()

number_tasks = []
number_tasks.append(slowly_add_two_numbers.s(1, 2))
number_tasks.append(slowly_add_two_numbers.s(3, 4))
number_tasks.append(slowly_add_two_numbers.s(5, 6))

final_number_task = slowly_add_two_numbers.si(7, 8)

chain_of_number_tasks = celery.chord(number_tasks, final_number_task)

print("Done")
