import logging

import flask

from monede.core.coins import Coins

app = flask.Flask(__name__)

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
monede = Coins()


@app.route('/all', methods=['GET'])
def get_all():
    return flask.jsonify(monede.all())


if __name__ == '__main__':
    app.run()
