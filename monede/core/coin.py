from monede.core.api import markets
from monede.core.api import trends


def massage(market, trend):
    data = []
    for mp, tp in zip(market[:-1], trend):
        data.append({
            'time': mp[0],  # doesn't matter if mp[0] or tp[0],
            'price': mp[4],
            'volume': mp[5],
            'trend': tp[1],
            'trades': mp[8]
        })
    return data


class Historical:
    # todo: parameters are overlapping in scope, merge timeframe into the rest
    def __init__(self, symbol, name):
        market = markets.coin_history(symbol=symbol)
        trend = trends.coin_trend(name=name, symbol=symbol)

        self.data = massage(market, trend)


class Snapshot:
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name
        self.historical = Historical(symbol, name)
