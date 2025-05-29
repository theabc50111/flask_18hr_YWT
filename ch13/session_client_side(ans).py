from flask import Flask, redirect, render_template, request, session, url_for
# ========== practice start ==========
from flask.sessions import SecureCookieSessionInterface
# ========== practice end ==========

app = Flask(__name__)
app.config["SECRET_KEY"] = "hard to guess string"


@app.route("/")
def index():
    return render_template("index.html", page_header="page_header")


# ========== practice start ==========
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        session["password"] = request.form["password"]
        return redirect(url_for("observe_session"))
    return render_template("login.html", page_header="Login")


@app.route("/observe_session")
def observe_session():
    # Use Flask's built-in session interface
    session_serializer = SecureCookieSessionInterface().get_signing_serializer(app)
    decoded_session = session_serializer.loads(request.cookies.get("session"))
    data = [
        ["base_url:", request.base_url],
        ["session:", session],
        ["request.cookies['session']:", request.cookies.get("session")],
        ["decoded_session:", decoded_session],
    ]
    return render_template(
        "observe_session.html", page_header="Session Data(client side)", data=data
    )
# ========== practice End ==========


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
