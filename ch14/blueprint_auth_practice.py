from functools import wraps
from pathlib import Path

# practice start
from flask import Flask, redirect, render_template, request, session, url_for

from flask_session import Session

# practice end


# practice start
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
# practice end
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
        return redirect(url_for("data_list"))
    return render_template("login.html", page_header="Login")


# practice start
# practice end
def logout():
    session.clear()
    return redirect(url_for("index"))
