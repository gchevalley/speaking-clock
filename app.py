from flask import Flask, jsonify, request

import datetime

app = Flask(__name__)

@app.route('/')
def entry_point():
    return jsonify({
        'host': request.host,
        'datetime': datetime.datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
