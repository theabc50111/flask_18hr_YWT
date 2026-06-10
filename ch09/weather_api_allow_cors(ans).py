from flask import Flask

app = Flask(__name__)


# ----------practice start------------
@app.route('/')
def index():
    return 'I am result of weather.com API that allowed cors!', 200, {'Access-Control-Allow-Origin': '*'}
# ----------practice end--------------


if __name__ == '__main__':
    # ----------practice start------------
    app.run(debug=True, host='0.0.0.0', port=5050)
    # ----------practice end--------------
