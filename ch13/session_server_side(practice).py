import hashlib
import pickle
import struct
import time
from pathlib import Path

from flask import Flask, redirect, render_template, request, session, url_for

# ========== practice start ==========
# ========== practice end ==========

app = Flask(__name__)
app.config["SECRET_KEY"] = "hard to guess string"
# ========== practice start ==========
# ========== practice end ==========


@app.route("/")
def index():
    return render_template("index.html", page_header="page_header")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        session["password"] = request.form["password"]
        return redirect(url_for("observe_session"))
    return render_template("login.html", page_header="Login")


# ========== practice start ==========
# ========== practice end ==========


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
