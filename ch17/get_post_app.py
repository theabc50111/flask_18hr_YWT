from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/test_get")
def test_get():
    return f"The method: {request.method}, args: {request.args}"


@app.route('/test_post', methods=['POST'])
def test_post():
    data = [["method:", request.method],
            ["base_url:", request.base_url],
            ["form data:", request.form]]
    return render_template('form_result.html', page_header="Form data", data=data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
