from flask import Flask, redirect, request
from flask_caching import Cache

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'SimpleCache'

cache = Cache(app)


# ========== practice start ==========
def init_cache_counter():
    cache.set('counter', 0)
# ========== practice end ==========


# ========== practice start ==========
@app.route('/get_cache_counter')
def get_cache_counter():
    val = cache.get('counter')
    return f"<h1> The counter value of cache: {val} <h1>"
# ========== practice end ==========


# ========== practice start ==========
@app.route('/set_cache_counter')
def set_cache_counter():
    set_val = request.args.get('set_val', type=int, default=-1)
    cache.set('counter', set_val)
    return redirect('/get_cache_counter')
# ========== practice end ==========


# ========== practice start ==========
@app.route('/del_cache_counter')
def del_cache_counter():
    cache.delete('counter')
    return redirect('/get_cache_counter')
# ========== practice end ==========


if __name__ == "__main__":
    init_cache_counter()
    app.run(debug=True, port=5000, host="0.0.0.0")
