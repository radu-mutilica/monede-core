import logging

import flask

from monede.core.server import Monede

app = flask.Flask(__name__)

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
monede = Monede()


@app.route('/all', methods=['GET'])
def get_all():
    return flask.jsonify(monede.get())


if __name__ == '__main__':
    app.run()
