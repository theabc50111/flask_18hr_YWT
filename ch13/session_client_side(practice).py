from flask import Flask, redirect, render_template, request, session, url_for
# ========== practice start ==========
# ========== practice end ==========

app = Flask(__name__)
app.config["SECRET_KEY"] = "hard to guess string"


@app.route("/")
def index():
    return render_template("index.html", page_header="page_header")


# ========== practice start ==========
# ========== practice End ==========


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
