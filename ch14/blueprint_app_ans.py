import math
from pathlib import Path

import sqlalchemy as db
from flask import Flask, render_template, request
from sqlalchemy import func

# practice start
from blueprint_auth_ans import auth_app, login_required
# practice end
from flask_session import Session

app = Flask(__name__)

# practice start
app.register_blueprint(auth_app)
# practice end
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


@app.route("/")
def index():
    return render_template("index.html", page_header="page_header")


@app.route("/data-list")
@login_required()
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
    print(app.url_map)  # To check the route `/login`, you can either watch it on a terminal or connect to /login through a browser
    app.run(debug=True, host="0.0.0.0", port=5000)
