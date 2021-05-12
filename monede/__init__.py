import logging

import flask
from flask_cors import CORS, cross_origin

from monede.core.server import Monede

app = flask.Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
monede = Monede()


@cross_origin()
@app.route('/api/v1/coins', methods=['GET'])
def coins():
    return flask.jsonify(monede.get())


if __name__ == '__main__':
    app.run()
