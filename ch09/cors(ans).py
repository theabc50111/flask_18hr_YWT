import uuid
from pathlib import Path

from flask import Flask, render_template, request, url_for

app = Flask(__name__)


# ----------practice start------------
@app.route('/')
def index():
    return render_template('cors(ans).html',
                           api_url_origin_allow_cors='http://192.168.0.17:5050/',
                           api_url_origin_not_allow_cors='http://192.168.0.17:5051/',  # press F12 to open dev tool, and check the console
                           page_header='Cross-Origin Resource Sharing (CORS) - Allow and Not Allow',)
# ----------practice end------------


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
