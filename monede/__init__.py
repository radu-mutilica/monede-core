import flask
from flask import request
from flask_cors import CORS, cross_origin

from monede.core import server

app = flask.Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@cross_origin()
@app.route('/api/v1/market', methods=['GET'])
def market():
    return flask.jsonify(server.coin_market(
        symbol=request.args['symbol'])
    )


@cross_origin()
@app.route('/api/v1/latest', methods=['GET'])
def latest_example():
    return flask.jsonify(server.latest_example())


@cross_origin()
@app.route('/api/v1/history', methods=['GET'])
def history():
    return flask.jsonify(server.coin_history(
        symbol=request.args['symbol'],
        timeframe=request.args.get('timeframe', 1))
    )


@cross_origin()
@app.route('/api/v1/top', methods=['GET'])
def top():
    return flask.jsonify(server.top())


@app.route('/ping', methods=['GET'])
def ping():
    return "pong"


if __name__ == '__main__':
    app.run()
