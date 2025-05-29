from flask import Flask, render_template

# practice start
from wrapper_init_auth import init_auth
# practice end

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", page_header="page_header")


init_auth(app)

if __name__ == "__main__":
    print(app.url_map)  # To check the route `/login`, you can either watch it on a terminal or connect to /login through a browser
    app.run(host="0.0.0.0", port=5000)
