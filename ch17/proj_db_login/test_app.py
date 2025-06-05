import pytest

from app import app


@pytest.fixture()
def test_flask_app():
    app.config["TESTING"] = True

    # other setup can go here
    yield app
    # clean up / reset resources here


@pytest.fixture()
def client(test_flask_app):
    return test_flask_app.test_client()


# USERS = {
#    "alice": {"password": "aliceP@ssw0rd", "role": "user"},
#    "bob": {"password": "bobP@ssw0rd", "role": "admin"},
# }
@pytest.mark.parametrize(
    argnames="username, password, role, expected_html",
    argvalues=[
        ("alice", "aliceP@ssw0rd", "user", "page of list all data"),
        ("bob", "bobP@ssw0rd", "admin", "page of list all data"),
        ("alice", "wrong_password", None, "Wrong password"),
        ("no_user", "whatever", None, "User not found"),
    ],
)
def test_login_valid_credentials(username, password, role, expected_html, client):
    """
    Simulate a successful login with valid user credentials
    """
    response = client.post(
        "/login",
        data={
            "username": username,
            "password": password,
        },
        follow_redirects=True,
    )
    # After login, user_id and role should be set in the session
    with client.session_transaction() as session:
        assert session.get("role") == role
    assert expected_html in response.data.decode("utf8")
    assert response.status_code == 200


@pytest.mark.parametrize(
    "form_data, is_raises_error",
    [
        ({"CustomerId": "1", "FirstName": "John", "LastName": "Doe"}, False),
        ({"CustomerId": "2", "FirstName": "", "LastName": "Smith"}, True),
        ({"CustomerId": "3"}, True),
    ],
)
def test_data_edit_post(client, mocker, form_data, is_raises_error):
    # Patch engine, connection, db, and table_customers
    mocker.patch("app.db")
    mocker.patch("app.engine")
    mocker.patch("app.table_customers")

    # Create session of role: admin
    with client.session_transaction() as session:
        session["username"] = "bob"
        session["role"] = "admin"

    # Simulate POST request
    if is_raises_error:
        with pytest.raises(ValueError, match="You should input the value of FirstName"):
            client.post("/data-edit", data=form_data)
    else:
        response = client.post("/data-edit", data=form_data)
        assert "Success" in response.data.decode("utf8")
