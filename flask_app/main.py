"""Flask App"""
import flasgger
import flask

from flask_app.blueprints import greetings

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
