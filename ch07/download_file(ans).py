from flask import Flask, render_template, request, send_from_directory
from pathlib import Path

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

@app.route('/')
def index():
    return render_template('index.html',
                           page_header="page_header")


# ----------practice start------------
@app.route('/download_file', methods=['GET', 'POST'])
def download_file():
    if request.method == "GET":
        return render_template('download.html', page_header="download file")
    elif request.method == "POST":
        file_name = request.form['download_file']
        file_dir = Path(__file__).resolve().parent/'uploaded'
    return send_from_directory(file_dir, file_name, as_attachment=True)  # as_attachment=False : render file by browser
# ----------practice end-----------

if __name__ == "__main__":
    app.run(debug=True)
