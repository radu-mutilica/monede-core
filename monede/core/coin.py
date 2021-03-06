from monede.core.api import exchange
from monede.core.api import trends


def massage(market, trend):
    data = []
    market = market[:-1]
    prices = [mp[4] for mp in market]
    min_price_1hr = min(prices)

    price_percentages = [100 - (float(min_price_1hr) / float(p)) * 100 for p in prices]

    for p, m, t in zip(price_percentages, market, trend):
        assert m[0] == t[0]  # todo: remove this once comfortable with data alignment

        data.append({
            'time': m[0],  # doesn't matter if mp[0] or tp[0],
            'price': p,
            'volume': float(m[5]),
            'trend': t[1],
            'trades': m[8]
        })
    return data


class Historical:
    def __init__(self, symbol, name, timeframe):
        market = exchange.coin_history(symbol=symbol, timeframe=timeframe.market)
        trend = trends.coin_trend(name=name, symbol=symbol, timeframe=timeframe.trend)

        self.data = massage(market, trend)

        # calculate the change in the timeframe, be it 1hr, 4hr, etc
        self.change_amount = self.data[-1]['price'] - self.data[0]['price']

        change_percentage = None
        idx = 0
        while not change_percentage:
            try:
                change_percentage = 100 - float(self.data[-1]['price']) / self.data[idx]['price']
            except ZeroDivisionError:
                idx += 1
            except IndexError:
                # we've iterated through all the self.data indexes and all price
                # values are zero, so there must be something wrong with the
                # data returned from the exchange API
                pass

            else:
                self.change_percentage = change_percentage


class Snapshot:
    def __init__(self, symbol, name, timeframe):
        self.symbol = symbol
        self.name = name
        self.historical = Historical(symbol, name, timeframe)
