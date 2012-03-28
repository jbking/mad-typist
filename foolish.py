import uuid
import random
from flask import Flask, make_response, request
app = Flask(__name__)

@app.route("/")
@app.route("/<path:dummy>")
def do_type(dummy=None):
    size = int(request.values.get('size', 100 * 1024))  # 100KiB

    t = '1234567890' \
        'abcdefghijklmnopqrstuvwxyz' \
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = make_response(''.join(random.choice(t) for _ in range(size)))
    res.headers['Content-Type'] = 'text/plain'
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res

app.run(debug=True)
