import time

from worker import app

@app.task(bind=True, name='slowly_reverse_string')
def slowly_reverse_string(self, string):
    ''' Reverse the string but take 10 seconds to do it '''
    n = 15
    for i in range(0, n):
        self.update_state(state='PROGRESS', meta={'done': i, 'total': n})
        time.sleep(1)
    return string[::-1]