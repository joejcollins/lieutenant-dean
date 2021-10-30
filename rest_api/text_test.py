""" Test the endpoint. """
import flask
import pytest
import rest_api.flask_app as flask_app
import rest_api.text as text


@pytest.fixture()
def app():
    """ Create a test fixture Flask application. """
    test_app = flask_app.rest_api
    test_app.register_blueprint(text.text_endpoints)
    return test_app


def test_reverse_fast(client):
    """ Return all the tags in use. """
    url = flask.url_for("text_api.reverse_fast")
    response = client.GET(url)
    # There were only 8 tags in use at the time of the recording.
    assert len(response.json) == 2
