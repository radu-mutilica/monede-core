import re

import time


def get_snapshot_timestamps():
    now = int(time.time() // 60 * 60)  # round down to nearest minute
    one_hour_ago = now - 3600
    return one_hour_ago, now


def sanitize(id):
    id = id.replace('-', ' ')
    return re.sub('[^A-Za-z0\\s]+', '', id)
