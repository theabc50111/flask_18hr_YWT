from flask import Flask, abort, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "hard to guess string"


@app.route("/valid_session")
def valid_session():
    if session["username"] == "test_user_1" and session["password"] == "1234":
        return "username & password correct"
    else:
        abort(401)
