from flask import Flask, jsonify, request
from flask_basicauth import BasicAuth

import os
import datetime

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = "john"
app.config['BASIC_AUTH_PASSWORD'] = "smith"
app.config['BASIC_AUTH_FORCE'] = True

basic_auth = BasicAuth(app)

@app.route('/')
def entry_point():
    return jsonify({
        'host': request.host,
        'datetime': datetime.datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001, ssl_context='adhoc')
