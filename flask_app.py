"""  """
import flask
import flasgger
import flasgger.utils as swag_utils
import flask_app_apidocs as apidocs
import strings.reverse as reverse

demo_api = flask.Flask(__name__)
demo_api.config['DEBUG'] = True
demo_api.register_blueprint(reverse.demo_api)

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
        'message': "Hello",
        'docs': '/apidocs/'
    }
    return flask.jsonify(greeting)
