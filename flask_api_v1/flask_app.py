""" Flask App """
import flask
import flasgger
import flasgger.utils as swag_utils
import flask_api_v1.flask_app_apidocs as apidocs
import flask_api_v1.text as text

api = flask.Flask(__name__)
api.register_blueprint(text.text_api)

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Celery Demo API",
        "description": "Demo of Flask and Celery in action.",
        "version": "0.0.1"
    },
    "basePath": "/"
}
swagger = flasgger.Swagger(api, template=swagger_template)


@api.route('/', methods=['GET'])
@swag_utils.swag_from(apidocs.INDEX)
def index():
    """ Confirm that the flask app is running. """
    greeting = {
        'message': "Hello there",
        'docs': '/apidocs/'
    }
    return flask.jsonify(greeting)
