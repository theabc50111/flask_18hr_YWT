import pytest

from app_practice import app


@pytest.fixture()
def test_flask_app():
    app.config["TESTING"] = True

    # other setup can go here
    yield app
    # clean up / reset resources here


@pytest.fixture()
def client(test_flask_app):
    return test_flask_app.test_client()

# ========== practice start ==========
# ========== practice end ==========
