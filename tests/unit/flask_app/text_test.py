"""Test the endpoint."""
import flask
import pytest

from flask_app.main import APP


@pytest.fixture()
def app():
    """Create a test fixture Flask application."""
    return APP


def xxx_test_reverse_fast_get(client) -> None:
    """Reverse a string with GET."""
    string_to_reverse = "qwerty"
    url = flask.url_for("text_api.reverse_fast_get",
                        string_to_reverse=string_to_reverse)
    response = client.get(url)
    # There were only 8 tags in use at the time of the recording.
    message = response.json
    assert len(message) == 2
    assert message['original'] == string_to_reverse
    assert message['reversed'] == 'ytrewq'


def xxx_test_reverse_fast_post(client) -> None:
    """Reverse a string with POST."""
    string_to_reverse = "asdfgh"
    url = flask.url_for("text_api.reverse_fast_post")
    post_message = {
        'string_to_reverse': string_to_reverse
    }
    response = client.post(url, json=post_message)
    message = response.json
    assert len(message) == 2
    assert message['original'] == string_to_reverse
    assert message['reversed'] == 'hgfdsa'
