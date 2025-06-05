import time

from flask import Flask
from flask_caching import Cache

app = Flask(__name__)

app.config['CACHE_TYPE'] = 'SimpleCache'
cache = Cache(app)


# Full Page Cache
@app.route('/')
@cache.cached(timeout=20)  # View cache for 20s
def index():
    for i in range(10, 0, -1):
        time.sleep(1)
        # WATCH SERVER CONSOLE: Simulating a countdown for rendering the page
        print(f"Rendering page countdown: {i} seconds remaining")
    return "<h1>Welcome to Cached Flask App</h1>"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
