from monede.core.api import markets
from monede.core.api import trends


def massage(market, trend):
    price_h, trend_h, volume_h = [], [], []
    for mp, tp in zip(market[1:-2], trend):
        price_h.append({
            'x': mp[0],  # doesn't matter if mp[0] or tp[0]
            # 'open_price': mp[1],
            # 'high_price': mp[2],
            # 'low_price': mp[3],
            'y': mp[4],
            # 'volume': mp[5],
            # 'trend': tp[1]
        })
        trend_h.append({
            'x': mp[0],  # doesn't matter if mp[0] or tp[0]
            'y': tp[1]
        })
        volume_h.append({
            'x': mp[0],  # doesn't matter if mp[0] or tp[0]
            'y': mp[5]
        })
    return {
        'price': price_h,
        'trend': trend_h,
        'volume': volume_h
    }


class Historical:
    # todo: parameters are overlapping in scope, merge timeframe into the rest
    def __init__(self, symbol, name, vs_currency, from_timestamp, to_timestamp,
                 timeframe):
        market = markets.coin_history(
            symbol=symbol,
            vs_currency=vs_currency,
            from_timestamp=from_timestamp,
            to_timestamp=to_timestamp)
        trend = trends.coin_trend(
            name=name,
            timeframe=timeframe)

        self.data = massage(market, trend)


class Snapshot:
    def __init__(self, symbol, name, vs_currency, from_timestamp, to_timestamp,
                 timeframe):
        self.symbol = symbol
        self.name = name
        self.historical = Historical(
            symbol,
            name,
            vs_currency,
            from_timestamp,
            to_timestamp,
            timeframe)
