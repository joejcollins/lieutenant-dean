""" Try the task executing it synchronously """
# import the celery tasks
from tasks import *

# Using `.s().apply()` will cause the task to execute immediately without Celery running
RESULT = slowly_reverse_string.s(string="qwerty").apply()

# Since the task is run synchronously this won't happened u
print("%s %s" % (RESULT.status, RESULT.ready()))

# The `.get()` will wait for the task to complete.
print(RESULT.get())
