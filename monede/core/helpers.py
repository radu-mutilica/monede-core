import re


def sanitize(id):
    id = id.replace('-', ' ')
    return re.sub('[^A-Za-z0\\s]+', '', id)


class Timeframe:
    def __init__(self, hours_ago):
        self.__hours_ago = hours_ago

        assert hours_ago in (1, 4), "Trends API only accepts certain timeframes"

        self.market = f"{hours_ago} hour ago UTC"
        self.trend = f"now {hours_ago}-H"
