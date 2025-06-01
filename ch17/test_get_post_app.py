import pytest
from markupsafe import Markup

from get_post_app import app


@pytest.fixture()
def test_flask_app():
    app.config["TESTING"] = True

    # other setup can go here
    yield app
    # clean up / reset resources here


@pytest.fixture()
def client(test_flask_app):
    return test_flask_app.test_client()


def test_get_request(client):
    response = client.get("/test_get", query_string={"a": 10, "b": "value_of_b"})
    print(f"***** {response.data} *****")
    assert response.status_code == 200
    assert "value_of_b" in response.data.decode("utf8")


def test_post_request(client):
    response = client.post(
            "/test_post",
            data={
                "email": "test_user@gmail.com",
                "passwords": "1234",
                "select1": "Open this select menu",
                "checkbox": "checkbox2",
                "radio1": "value2",
            }
        )
    tbl_html_str = "\n".join(response.data.decode("utf8").split("\n")[70:100])
    print(f"{Markup(tbl_html_str).unescape()}")
    assert response.status_code == 200
    assert "test_user@gmail.com" in response.data.decode("utf8")
