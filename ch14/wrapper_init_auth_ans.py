from flask import Flask, redirect, render_template, request, session, url_for

from flask_session import Session

USERS = {
    "alice": {"password": "aliceP@ssw0rd", "role": "user"},
    "bob": {"password": "bobP@ssw0rd", "role": "admin"},
}


# ========== practice start ==========
def init_auth(app):
# ========== practice end ==========
    @app.route("/login", methods=["GET", "POST"])
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
            return redirect(url_for("/"))
        return render_template("login.html", page_header="Login")
