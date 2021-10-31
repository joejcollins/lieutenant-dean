""" Text endpoints. """
import flask
import flasgger.utils as swag_utils
import rest_api.text_apidocs as apidocs
import my_module.text as data_text

text_api = flask.Blueprint("text_api", __name__, url_prefix="/text/")


def _reverse_fast(string_to_reverse):
    """ Provide a json response with the reversal. """
    reversed_string = data_text.reverse_text(string_to_reverse)
    message = {
        'original': string_to_reverse,
        'reversed': reversed_string
    }
    return message


@text_api.route('/reverse/fast/<string_to_reverse>', methods=['GET'])
@swag_utils.swag_from(apidocs.REVERSE_GET)
def reverse_fast_get(string_to_reverse):
    """ Provide a json response with the reversal. """
    message = _reverse_fast(string_to_reverse)
    return flask.jsonify(message)


@text_api.route('/reverse/fast', methods=['POST'])
@swag_utils.swag_from(apidocs.REVERSE_POST)
def reverse_fast_post():
    """ Provide a json response with the reversal. """
    string_to_reverse = flask.request.json.get("string_to_reverse")
    message = _reverse_fast(string_to_reverse)
    return flask.jsonify(message)
