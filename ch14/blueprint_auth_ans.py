from functools import wraps
from pathlib import Path

# practice start
from flask import (Blueprint, Flask, redirect, render_template, request,
                   session, url_for)

from flask_session import Session

# practice end


# practice start
auth_app = Blueprint('auth_app', __name__)
# practice end

USERS = {
    "alice": {"password": "aliceP@ssw0rd", "role": "user"},
    "bob": {"password": "bobP@ssw0rd", "role": "admin"},
}


def login_required(role=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if "username" not in session:
                # practice start
                return redirect(url_for("auth_app.login"))
                # practice start
            if role and session.get("role") != role:
                print(f"session.get('role')={session.get('role')}, role={role}")
                return render_template(
                    "index.html",
                    page_header="Access Denied",
                )
            return f(*args, **kwargs)

        return wrapper

    return decorator


# practice start
@auth_app.route("/login", methods=["GET", "POST"])
# practice end
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        session["password"] = request.form["password"]
        if session["username"] not in USERS.keys():
            return render_template("index.html", page_header="User not found")
        elif session["password"] != USERS.get(session["username"]).get("password"):
            return render_template("index.html", page_header="Wrong password")
        else:
            session["role"] = USERS.get(session["username"]).get("role")
        return redirect(url_for("data_list"))
    return render_template("login.html", page_header="Login")


# practice start
@auth_app.route("/logout")
# practice end
def logout():
    session.clear()
    return redirect(url_for("index"))
