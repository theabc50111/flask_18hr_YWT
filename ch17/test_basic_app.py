import pytest

from basic_app import app


@pytest.fixture()
def test_flask_app():
    app.config["TESTING"] = True

    # other setup can go here
    yield app
    # clean up / reset resources here


@pytest.fixture()
def client(test_flask_app):
    return test_flask_app.test_client()


def test_index_request(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"<h1>Hello World!</h1>" in response.data
