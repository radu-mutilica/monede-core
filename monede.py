import flask
from flask import jsonify
from core.api import coins
app = flask.Flask(__name__)


@app.route('/api/v1/coins/all', methods=['GET'])
def coins():
    return jsonify(sorted(coins.all(), key=lambda x: x['price_change_percentage_24h'], reverse=True))


if __name__ == '__main__':
    app.run()
