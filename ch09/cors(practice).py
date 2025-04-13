import uuid
from pathlib import Path

from flask import Flask, render_template, request, url_for

app = Flask(__name__)


# ----------practice start------------
# ----------practice end------------


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
