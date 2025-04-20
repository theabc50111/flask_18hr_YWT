import hashlib
import pickle
import struct
import time
from pathlib import Path

from flask import Flask, redirect, render_template, request, session, url_for

# ========== practice start ==========
from flask_session import Session
# ========== practice end ==========

app = Flask(__name__)
app.config["SECRET_KEY"] = "hard to guess string"
# ========== practice start ==========
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_FILE_DIR"] = Path(__file__).parent / "flask_session"
Session(app)
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
@app.route("/observe_session")
def observe_session():
    session_id = request.cookies.get("session")
    session_file_encode_prefix = app.config.get("SESSION_FILE_PREFIX", "session:")
    key = f"{session_file_encode_prefix}{session_id}"
    session_file_name = hashlib.md5(key.encode("utf-8")).hexdigest()
    with open(app.config["SESSION_FILE_DIR"] / f"{session_file_name}", "rb") as f:
        timeout_bytes = f.read(4)
        (expires_at,) = struct.unpack("I", timeout_bytes)
        if expires_at < int(time.time()):
            session.clear()
            return redirect(url_for("login"))
        session_data = pickle.load(f)
    data = [
        ["base_url:", request.base_url],
        ["session:", session],
        ["request.cookies['session']:", request.cookies.get("session")],
        ["session_file_name:", session_file_name],
        ["session_file_path:", app.config["SESSION_FILE_DIR"] / f"{session_file_name}"],
        ["session_data:", session_data],
    ]
    return render_template(
        "observe_session.html", page_header="Session Data(server side)", data=data
    )
# ========== practice end ==========


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
