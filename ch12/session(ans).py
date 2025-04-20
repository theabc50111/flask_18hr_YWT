# practice start
from flask import Flask, render_template, request, redirect, url_for, session
# practice end

app = Flask(__name__)

# practice start
app.config['SECRET_KEY'] = 'hard to guess string'
# practice end

@app.route('/')
def index():
    return render_template('index.html',
                           page_header="Index")


# practice start
@app.route('/session', methods=['GET', 'POST'])
def get_session():
    if request.method == "POST":
        session["form_data"] = request.form
        return redirect(url_for("get_session"))
    data = [["method:", request.method],
            ["base_url:", request.base_url],
            ["form data:", request.form],
            ["session:", session],
            ["session['form_data']:", session.get("form_data")]]
    return render_template('session.html', page_header="Form", data=data)
# practice end
 

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
