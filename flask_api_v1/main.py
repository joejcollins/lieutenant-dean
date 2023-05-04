""" Flask App """
import flask
import flasgger
import flasgger.utils as swag_utils
from flask_api_v1.blueprints import greetings

APP = flask.Flask(__name__)
APP.register_blueprint(greetings.APP)

SWAGGER_TEMPLATE = {
    "swagger": "2.0",
    "info": {
        "title": "Flask API",
        "description": "Demo of Flask action.",
        "version": "0.0.1"
    },
    "basePath": "/"
}
flasgger.Swagger(APP, template=SWAGGER_TEMPLATE)
