from flask import Flask, render_template

import circular_auth

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", page_header="page_header")



if __name__ == "__main__":
    print(app.url_map)
    app.run(host="0.0.0.0", port=5000)
