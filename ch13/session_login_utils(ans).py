import math
from pathlib import Path

import sqlalchemy as db
from sqlalchemy import func
from functools import wraps
from flask import Flask, redirect, render_template, request, session, url_for

from flask_session import Session

app = Flask(__name__)
app.config["SECRET_KEY"] = "hard to guess string"
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_FILE_DIR"] = Path(__file__).parent / "flask_session"
Session(app)

# sql setting
path_to_db = "./db/chinook.db"
table = "customers"
engine = db.create_engine(f"sqlite:///{path_to_db}")
metadata = db.MetaData()
table_customers = db.Table(table, metadata, autoload_with=engine)

USERS = {
    "alice": {"password": "aliceP@ssw0rd", "role": "user"},
    "bob": {"password": "bobP@ssw0rd", "role": "admin"},
}


# ========== practice start ==============
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
# ========== practice end ==============


@app.route("/")
def index():
    return render_template("index.html", page_header="page_header")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        session["password"] = request.form["password"]
        # ========== practice start ==============
        if session["username"] not in USERS.keys():
            return render_template("index.html", page_header="User not found")
        elif session["password"] != USERS.get(session["username"]).get("password"):
            return render_template("index.html", page_header="Wrong password")
        else:
            session["role"] = USERS.get(session["username"]).get("role")
        # ========== practice end ==============
        return redirect(url_for("data_list"))
    return render_template("login.html", page_header="Login")


# ========== practice start ==============
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))
# ========== practice end ==============


@app.route("/data-list")
# ========== practice start ==============
@login_required()
# ========== practice end ==============
def data_list():
    # query string
    page = int(request.args.get("page") if request.args.get("page") else 1)
    each_page = 5

    # set total pages
    connection = (
        engine.connect()
    )  # connection 要放在view function中，否則會出現thread error
    query = db.select(func.count()).select_from(table_customers)
    proxy = connection.execute(query)
    total_pages = math.ceil(
        proxy.fetchall()[0][0] / each_page
    )  # [0][0] => inorder to get the value

    # fetch data & decided by page
    query = db.select(table_customers).limit(each_page).offset((page - 1) * each_page)
    proxy = connection.execute(query)
    results = proxy.fetchall()
    print(table_customers.columns.keys())

    # Close connection
    connection.close()

    return render_template(
        "data_list.html",
        page_header="list all data",
        total_pages=total_pages,
        outputs=results,
        page=page,
    )


@app.route("/data-edit", methods=["GET", "POST"])
# ========== practice start ==============
@login_required(role="admin")
# ========== practice end ==============
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
        except:
            return render_template(
                "data_edit.html",
                page_header="edit data",
                id_list=id_list,
                status="Failed",
            )
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
