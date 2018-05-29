from flask import Flask, jsonify, request
from flask_basicauth import BasicAuth

import os
import datetime

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = os.environ['FLASK_AUTH_USERNAME']
app.config['BASIC_AUTH_PASSWORD'] = os.environ['FLASK_AUTH_PASSWORD']
app.config['BASIC_AUTH_FORCE'] = True

basic_auth = BasicAuth(app)

@app.route('/')
def entry_point():
    return jsonify({
        'host': request.host,
        'datetime': datetime.datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
