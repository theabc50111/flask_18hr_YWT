from flask import Flask

app = Flask(__name__)


# ----------practice start------------
@app.route('/')
def index():
    return 'I am result of bank.com API that NOT allowed cors!', 200
# ----------practice end--------------


if __name__ == '__main__':
    # ----------practice start------------
    app.run(debug=True, host='0.0.0.0', port=5051)
    # ----------practice end--------------
