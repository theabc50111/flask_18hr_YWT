import time
from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           page_header="index page")


# ----------practice start------------
@app.route('/long_proc')
def long_proc():
    time.sleep(10)
    return render_template('index.html',
                           page_header="waited for long proc")
# ----------practice end------------


if __name__ == "__main__":
    # ----------practice start------------
    app.run(debug=True, host="0.0.0.0", threaded=False)
    # ----------practice end------------
