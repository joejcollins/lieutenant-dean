""" Text endpoints. """
import flask
import flasgger.utils as swag_utils
import rest_api.text_apidocs as apidocs
import my_module.text as data_text

endpoints = flask.Blueprint("auth", __name__, url_prefix="/text/")

@endpoints.route('/reverse/fast/<string_to_reverse>', methods=['GET', 'POST'])
@swag_utils.swag_from(apidocs.REVERSE)
def reverse(string_to_reverse):
    """ Provide a json response with the reversal. """
    reversed_string = data_text.reverse_text(string_to_reverse)
    message = {
        'original': string_to_reverse,
        'reversed': reversed_string
    }
    return flask.jsonify(message)
