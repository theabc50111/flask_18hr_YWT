from flask import Flask, make_response, redirect, request, url_for

app = Flask(__name__)


@app.route("/")
def index():
    # 讀取 Cookie (後端讀得到)
    cookie_user = request.cookies.get("cookie_user", "❌ 找不到 Cookie")

    # 這裡移除 f-string，改用傳統的 .format()，這樣 JS 的大括號 {} 只要正常寫就好，完全不會衝突！
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cookie vs SessionStorage</title>
        <style>
            body { font-family: sans-serif; margin: 40px; line-height: 1.6; color: #333; }
            .container { display: flex; gap: 20px; max-width: 800px; }
            .box { flex: 1; border: 2px solid #ccc; padding: 20px; border-radius: 8px; }
            .cookie-box { border-color: #007BFF; background: #f0f7ff; }
            .storage-box { border-color: #28a745; background: #f1fcf4; }
            button { padding: 10px 15px; background: #222; color: white; border: none; border-radius: 4px; cursor: pointer; }
            input { padding: 8px; width: 80%; margin-bottom: 10px; }
            hr { border: 0; border-top: 1px solid #eee; margin: 15px 0; }
        </style>
    </head>
    <body>
        <h2>實驗室：觀察 Cookie 與 SessionStorage 的異同</h2>
        <p>💡 提示：請同時開啟<strong>多個分頁</strong>來觀察對照！</p>

        <div class="container">
            <div class="box cookie-box">
                <h3>1. Cookie 狀態 (後端+前端皆可控)</h3>
                <p>目前數值: <strong id="cookie-val">__COOKIE_USER__</strong></p>
                <form action="/set_cookie" method="POST">
                    <input type="text" name="username" required placeholder="輸入 Cookie 內容">
                    <button type="submit">寫入 Cookie</button>
                </form>
            </div>

            <div class="box storage-box">
                <h3>2. SessionStorage 狀態 (純前端控制)</h3>
                <p>目前數值: <strong id="storage-val">⏳ 載入中...</strong></p>
                <input type="text" id="storage-input" placeholder="輸入 SessionStorage 內容">
                <button onclick="saveSessionStorage()">寫入 SessionStorage</button>
            </div>
        </div>

        <br/>
        <button onclick="window.location.reload()" style="background:#6c757d;">🔄 重新整理本頁 (或手動按 F5)</button>

        <script>
            // 頁面載入時，從瀏覽器取出 SessionStorage 並顯示在畫面上
            document.addEventListener("DOMContentLoaded", function() {
                const sessionVal = sessionStorage.getItem("session_user");
                document.getElementById("storage-val").innerText = sessionVal ? sessionVal : "❌ 找不到 SessionStorage";
            });

            // 寫入 SessionStorage 的前端 JS 函式
            function saveSessionStorage() {
                const val = document.getElementById("storage-input").value;
                if (!val) return alert("請輸入內容！");
                sessionStorage.setItem("session_user", val);
                document.getElementById("storage-val").innerText = val;
            }
        </script>
    </body>
    </html>
    """.replace(
        "__COOKIE_USER__", cookie_user
    )  # 用單純的 replace 替換變數，最安全


# 處理寫入 Cookie 的路由
@app.route("/set_cookie", methods=["POST"])
def set_cookie():
    username = request.form.get("username")
    response = make_response(redirect(url_for("index")))
    # 寫入一個簡單的 Cookie
    response.set_cookie("cookie_user", username, samesite="Lax")
    return response


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
