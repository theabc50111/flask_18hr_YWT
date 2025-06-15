from functools import wraps
from pathlib import Path

from flask import Flask, redirect, render_template, request, session, url_for

from flask_session import Session

app = Flask(__name__)
app.config["SECRET_KEY"] = "hard to guess string"
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_FILE_DIR"] = Path(__file__).parent / "flask_session"
Session(app)


USERS = {
    "alice": {"password": "aliceP@ssw0rd", "role": "user"},
    "bob": {"password": "bobP@ssw0rd", "role": "admin"},
}
# ========== practice start ==============
# ========== practice end ==============


def login_required(role=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if "username" not in session:
                return redirect(url_for("login"))
            if role and session.get("role") != role:
                print(f"session.get('role')={session.get('role')}, role={role}")
                return render_template(
                    "index.html",
                    page_header="Access Denied",
                )
            return f(*args, **kwargs)

        return wrapper

    return decorator


@app.route("/")
def index():
    return render_template("index.html", page_header="page_header")


@app.route("/login", methods=["GET", "POST"])
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


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route("/data-list")
@login_required()
def data_list():
    return "page of list all data"


@app.route("/data-edit", methods=["GET", "POST"])
@login_required(role="admin")
def data_edit():
    if request.method == "POST":
        try:
            connection = (
                engine.connect()
            )  # connection 要放在view function中，否則會出現thread error

            query = db.select(table_customers.c.CustomerId).order_by(
                table_customers.c.CustomerId
            )

            proxy = connection.execute(query)
            id_list = [idx[0] for idx in proxy.fetchall()]
            if request.form["FirstName"]:  # 希望至少要填寫名子
                query = (
                    db.update(table_customers)
                    .where(table_customers.c.CustomerId == request.form["CustomerId"])
                    .values(**request.form)
                )
                connection.execute(query)
                connection.commit()
            else:
                raise Exception
        # ========== practice start ==============
        # ========== practice end ==============
        else:
            return render_template(
                "data_edit.html",
                page_header="edit data",
                id_list=id_list,
                status="Success",
            )
        finally:
            # Close connection
            connection.close()

    if request.method == "GET":
        connection = (
            engine.connect()
        )  # connection 要放在view function中，否則會出現thread error
        query = db.select(table_customers.c.CustomerId).order_by(
            table_customers.c.CustomerId
        )
        proxy = connection.execute(query)
        id_list = [idx[0] for idx in proxy.fetchall()]
        connection.close()
        return render_template(
            "data_edit.html", page_header="edit data", id_list=id_list
        )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
