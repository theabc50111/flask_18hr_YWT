import pytest

from session_app import app


@pytest.fixture()
def test_flask_app():
    app.config["TESTING"] = True

    # other setup can go here
    yield app
    # clean up / reset resources here


@pytest.fixture()
def client(test_flask_app):
    return test_flask_app.test_client()


@pytest.mark.parametrize(
    argnames=["arg_uname", "arg_pwd", "expected_status_code"],
    argvalues=[
        ("test_user_1", "1234", 200),
        ("test_user_1", "5678", 401),
    ],
)
def test_get_with_session(arg_uname, arg_pwd, expected_status_code, client):
    with client.session_transaction() as session:
        session["username"] = arg_uname
        session["password"] = arg_pwd

    response = client.get("/valid_session")
    assert response.status_code == expected_status_code
