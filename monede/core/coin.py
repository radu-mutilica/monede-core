from monede.core.api import markets
from monede.core.api import trends


def massage(market, trend):
    data = []
    for mp, tp in zip(market[1:-2], trend):
        data.append({
            'close_time': mp[0],  # doesn't matter if mp[0] or tp[0]
            'open_price': mp[1],
            'high_price': mp[2],
            'low_price': mp[3],
            'close_price': mp[4],
            'volume': mp[5],
            'trend': tp[1]
        })
    return data


class Historical:
    # todo: parameters are overlapping in scope, merge timeframe into the rest
    def __init__(self, id, vs_currency, from_timestamp, to_timestamp, timeframe):
        market = markets.coin_history(
            id=id,
            vs_currency=vs_currency,
            from_timestamp=from_timestamp,
            to_timestamp=to_timestamp)
        trend = trends.coin_trend(
            id=id,
            timeframe=timeframe)

        self.data = massage(market, trend)


class Snapshot:
    def __init__(self, id, name, vs_currency, from_timestamp, to_timestamp, timeframe):
        self.id = id
        self.name = name
        self.historical = Historical(
            id,
            vs_currency,
            from_timestamp,
            to_timestamp,
            timeframe)
