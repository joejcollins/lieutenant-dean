"""  """
import flask
import flasgger
import flasgger.utils as swag_utils
import api.flask_app_apidocs as apidocs
import api.text as text

rest_api = flask.Flask(__name__)
rest_api.register_blueprint(text.endpoints)

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Celery Demo API",
        "description": "Demo of Flask and Celery in action.",
        "version": "0.0.1"
    },
    "basePath": "/"
}
swagger = flasgger.Swagger(rest_api, template=swagger_template)


@rest_api.route('/', methods=['GET'])
@swag_utils.swag_from(apidocs.INDEX)
def index():
    """ Confirm that the flask app is running. """
    greeting = {
        'message': "Hello there",
        'docs': '/apidocs/'
    }
    return flask.jsonify(greeting)
