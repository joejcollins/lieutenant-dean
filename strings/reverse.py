
""" Thinking about reversing strings.  """
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
    return string[::-1]


@demo_api.route('/', methods=['POST'])
def reverse():
    """  """
    if flask.request.method == 'POST':
        tasks.slowly_reverse_string.s(url=request.json['url']).delay()
        return jsonify({'url': request.json['url']}), 201

    data = os.listdir(PATH) if os.path.exists(PATH) else []
    return jsonify(data)


def reverse_this(string_to_reverse):
    """ Do the string reversal. """
    reversed_string = string_to_reverse[::-1]

