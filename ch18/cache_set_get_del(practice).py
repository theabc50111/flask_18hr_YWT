from flask import Flask, redirect, request
from flask_caching import Cache

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'SimpleCache'

cache = Cache(app)


# ========== practice start ==========
# ========== practice end ==========


# ========== practice start ==========
# ========== practice end ==========


# ========== practice start ==========
# ========== practice end ==========


# ========== practice start ==========
# ========== practice end ==========


if __name__ == "__main__":
    init_cache_counter()
    app.run(debug=True, port=5000, host="0.0.0.0")
