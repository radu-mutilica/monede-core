import os
import json

from monede.settings import NOTIFICATIONS_DB_PATH


def _init_db(path):
    if not os.path.exists(path):
        os.makedirs(path)

def _get(path, backend):
    with open(path, 'rb') as f:
        return backend.load(f)

class NotificationDB:
    def __init__(self, path=NOTIFICATIONS_DB_PATH, serialization_backend=json):
        self._path = path
        self._backend = json
        self._latest_notification_path = os.path.join(path, 'latest')
        _init_db(path)

    def get_latest(self):
        return _get(self._latest_notification_path, self._backend)



