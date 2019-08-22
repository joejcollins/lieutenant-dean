""" Task list for Celery  """
# The task needs to run for a long time
import time

# The app provides the Celery configuration.
from worker import app

@app.task(bind=True, name='slowly_reverse_string')
def slowly_reverse_string(self, string):
    """ Reverse the string but take 10 seconds to do it """
    counter = 10
    for i in range(0, counter):
        self.update_state(state='PROGRESS', meta={'done': i, 'total': counter })
        time.sleep(1)
    import pdb; pdb.set_trace()
    return string[::-1]
