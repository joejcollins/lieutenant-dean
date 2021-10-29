"""  """
import flask
import flasgger
import flasgger.utils as swag_utils
import api.flask_app_apidocs as apidocs
import api.text as text

demo_api = flask.Flask(__name__)
demo_api.register_blueprint(text.endpoints)

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Celery Demo API",
        "description": "Demo of Flask and Celery in action.",
        "version": "0.0.1"
    },
    "basePath": "/"
}
swagger = flasgger.Swagger(demo_api, template=swagger_template)


@demo_api.route('/', methods=['GET'])
@swag_utils.swag_from(apidocs.INDEX)
def index():
    """ Confirm that the flask app is running. """
    greeting = {
        'message': "Hello there",
        'docs': '/apidocs/'
    }
    return flask.jsonify(greeting)
