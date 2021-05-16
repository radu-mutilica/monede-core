from monede.core.api import markets
from monede.core.api import trends


def massage(market, trend):
    data = []
    market = market[:-1]
    prices = [mp[4] for mp in market]
    min_price_1hr = min(prices)

    price_percentages = [100 - (float(min_price_1hr) / float(p)) * 100 for p in prices]

    for p, m, t in zip(price_percentages, market, trend):
        data.append({
            'time': m[0],  # doesn't matter if mp[0] or tp[0],
            'price': p,
            'volume': float(m[5]),
            'trend': t[1],
            'trades': m[8]
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
