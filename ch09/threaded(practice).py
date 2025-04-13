import time
import uuid
from pathlib import Path

from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           page_header="index page")


# ----------practice start------------
# ----------practice end------------


if __name__ == "__main__":
    # ----------practice start------------
    # ----------practice end------------
