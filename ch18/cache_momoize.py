import time

from flask import Flask, request
from flask_caching import Cache

app = Flask(__name__)

app.config['CACHE_TYPE'] = 'SimpleCache'
cache = Cache(app)


@app.route('/get_computation')
def get_computation():
    result = slow_compute(request.args.get('n', default=1, type=int))
    return f"<h1>result of slow_compute() = {result}</h1>"


@cache.memoize(timeout=180)
def slow_compute(n):
    # the cache key is based on the function name and its arguments
    # so if you call slow_compute(1) and then slow_compute(2), the results will be cached separately
    for i in range(10, 0, -1):
        time.sleep(1)
        print(f"Computing: {i} seconds remaining")
    return n * 10


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
