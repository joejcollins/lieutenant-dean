import flask
from flasgger.utils import swag_from
from flask_app_v1.apidocs import greetings as greetings_docs

APP = flask.Blueprint("greetings", __name__, url_prefix='/greetings')

@APP.route('/', methods=['GET'])
@swag_from(greetings_docs.INDEX)
def index() -> dict:
    """ Confirm that the flask app is running. """
    return {'message': "Hello there", 'docs': '/apidocs/'}
