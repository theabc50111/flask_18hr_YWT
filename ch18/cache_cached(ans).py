import time

from flask import Flask
# ========== practice start ==========
from flask_caching import Cache
# ========== practice end ==========

app = Flask(__name__)

# ========== practice start ==========
app.config['CACHE_TYPE'] = 'SimpleCache'
cache = Cache(app)
# ========== practice end ==========


# ========== practice start ==========
# Full Page Cache
@app.route('/')
@cache.cached(timeout=20)  # View cache for 20s
def index():
    for i in range(10, 0, -1):
        time.sleep(1)
        # WATCH SERVER CONSOLE: Simulating a countdown for rendering the page
        print(f"Rendering page countdown: {i} seconds remaining")
    return "<h1>Welcome to Cached Flask App</h1>"
# ========== practice end ==========


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
