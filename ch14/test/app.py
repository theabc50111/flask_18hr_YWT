from flask import Flask

import userdata

app = Flask(__name__)
userdata.init_app(app)


@app.route('/')
def index():
    return 'foo'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
