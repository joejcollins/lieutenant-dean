
""" Thinking about reversing strings.  """
# The task needs to run for a long time
import time
import flask
import flasgger.utils as swag_utils
import strings.reverse_apidocs as apidocs
# import celery.worker.app as celery

demo_api = flask.Blueprint("auth", __name__, url_prefix="/reverse/")


@demo_api.route('/fast/<string_to_reverse>', methods=['POST'])
@swag_utils.swag_from(apidocs.REVERSE)
def reverse(string_to_reverse):
    """ Provide a json response with the reversal. """
    reversed_string = reverse_this(string_to_reverse)
    message = {
        'original': string_to_reverse,
        'reversed': reversed_string
    }
    return flask.jsonify(message)


# The app provides the Celery configuration.
# from worker import app

# @celery.task(bind=True, name='slowly_reverse_string')
# def slowly_reverse_string(self, string):
#     """ Reverse the string but take 10 seconds to do it """
#     counter = 10
#     for i in range(0, counter):
#         self.update_state(state='PROGRESS', meta={'done': i, 'total': counter })
#         time.sleep(1)
#     return string[::-1]


def reverse_this(string_to_reverse):
    """ Do the string reversal. """
    reversed_string = string_to_reverse[::-1]
    return reversed_string
