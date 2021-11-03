""" Text endpoints. """
import flask
import flasgger.utils as swag_utils
import rest_api.text_apidocs as apidocs
import info_module.text as info_text
import task_queue.text as text_tasks

text_api = flask.Blueprint("text_api", __name__, url_prefix="/text/")


def _reverse_fast(string_to_reverse):
    """ Provide a json response with the reversal. """
    reversed_string = info_text.reverse_string(string_to_reverse)
    message = {
        'original': string_to_reverse,
        'reversed': reversed_string
    }
    return message


@text_api.route('/reverse/fast/<string_to_reverse>', methods=['GET'])
@swag_utils.swag_from(apidocs.REVERSE_FAST_GET)
def reverse_fast_get(string_to_reverse):
    """ Provide a json response with the reversal. """
    message = _reverse_fast(string_to_reverse)
    return flask.jsonify(message)


@text_api.route('/reverse/fast', methods=['POST'])
@swag_utils.swag_from(apidocs.REVERSE_FAST_POST)
def reverse_fast_post():
    """ Provide a json response with the reversal. """
    string_to_reverse = flask.request.json.get("string_to_reverse")
    message = _reverse_fast(string_to_reverse)
    return flask.jsonify(message)


@text_api.route('/reverse/slow/<string_to_reverse>', methods=['GET'])
@swag_utils.swag_from(apidocs.REVERSE_SLOW_GET)
def reverse_slow_get(string_to_reverse):
    """ Provide a json response with the reversal. """
    result = text_tasks.slowly_reverse_string.delay(
        string_to_reverse=string_to_reverse
        )
    result_dict = vars(result)
    # Filter the dictionary to send back.
    result_dict = {
        k: v for (k, v) in result_dict.items()
        if isinstance(v, (str, bool, int))
        }
    return flask.jsonify(result_dict)
