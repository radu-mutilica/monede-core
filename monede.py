import flask
from flask import jsonify

app = flask.Flask(__name__)


@app.route('/api/v1/coins/all', methods=['GET'])
def api_all():
    return jsonify(['bitcoin', 'ethereum'])


if __name__ == '__main__':
    app.run()
