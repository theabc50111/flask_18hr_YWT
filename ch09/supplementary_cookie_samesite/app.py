from flask import Flask, make_response, redirect, request, url_for

app = Flask(__name__)


# 模擬一個簡單的 HTML 頁面
def get_html_template(content: str) -> str:
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cookie Shared Demo</title>
        <style>
            body {{ font-family: sans-serif; margin: 40px; line-height: 1.6; }}
            .card {{ border: 1px solid #ccc; padding: 20px; border-radius: 8px; max-width: 400px; }}
            button {{ padding: 8px 16px; background: #007BFF; color: white; border: none; border-radius: 4px; cursor: pointer; }}
            button.logout {{ background: #DC3545; }}
        </style>
    </head>
    <body>
        <h2>Flask Cookie 共用實驗室</h2>
        <div class="card">
            {content}
        </div>
    </body>
    </html>
    """


@app.route("/")
def index():
    # 嘗試從瀏覽器請求中讀取名為 'username' 的 Cookie
    username = request.cookies.get("username")

    if username:
        # 如果有 Cookie，顯示歡迎訊息與登出按鈕
        content = f"""
        <p>✅ 偵測到 Cookie！</p>
        <p>目前登入的身分是: <strong>{username}</strong></p>
        <form action="/logout" method="POST">
            <button class="logout" type="submit">安全登出（清除 Cookie）</button>
        </form>
        """
        return get_html_template(content)

    # 如果沒有 Cookie，顯示登入表單
    content = """
    <p>❌ 目前尚未登入（找不到 Cookie）</p>
    <form action="/login" method="POST">
        <label>輸入隨便一個名字登入: </label><br/><br/>
        <input type="text" name="username" required placeholder="例如: Alex"><br/><br/>
        <button type="submit">登入（寫入 Cookie）</button>
    </form>
    """
    return get_html_template(content)


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    response = make_response(redirect(url_for("index")))

    # 關鍵：寫入 Cookie。
    # 這裡我們顯式設定 samesite=None 和 secure=False 方便本機 http 測試
    response.set_cookie("username", username, samesite="Lax")
    return response


@app.route("/logout", methods=["POST"])
def logout():
    response = make_response(redirect(url_for("index")))
    # 清除 Cookie（透過將過期時間設為過去）
    response.delete_cookie("username")
    return response


if __name__ == "__main__":
    # 啟動在本機 5000 埠口
    app.run(debug=True, port=5000, host="0.0.0.0")
