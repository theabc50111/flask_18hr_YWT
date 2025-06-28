from functools import wraps
from pathlib import Path

from flask import (Blueprint, Flask, redirect, render_template, request,
                   session, url_for)

from flask_session import Session

# ========== practice start ==========
blueprint_options_auth_app = Blueprint('blueprint_options_auth_app', __name__, url_prefix="/auth", template_folder='blueprint_options_auth_templates', static_folder='blueprint_options_auth_static')
# ========== practice end ==========

USERS = {
    "alice": {"password": "aliceP@ssw0rd", "role": "user"},
    "bob": {"password": "bobP@ssw0rd", "role": "admin"},
}


def login_required(role=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if "username" not in session:
                return redirect(url_for("blueprint_options_auth_app.login"))
            if role and session.get("role") != role:
                print(f"session.get('role')={session.get('role')}, role={role}")
                return render_template(
                    "index.html",
                    page_header="Access Denied",
                )
            return f(*args, **kwargs)

        return wrapper

    return decorator


@blueprint_options_auth_app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] not in USERS.keys():
            return render_template("index.html", page_header="User not found")
        elif request.form["password"] != USERS.get(request.form["username"]).get("password"):
            return render_template("index.html", page_header="Wrong password")
        else:
            session["username"] = request.form["username"]
            session["password"] = request.form["password"]
            session["role"] = USERS.get(session["username"]).get("role")
    # ========== practice start ==========
    return render_template("new_login(ans).html")
    # ========== practice end ==========


@blueprint_options_auth_app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))
