from pytrends.request import TrendReq
from monede.core.helpers import sanitize

_pytrends = TrendReq()


def coin_trend(id, timeframe):
    _pytrends.build_payload([sanitize(id)], timeframe=timeframe)
    interest = _pytrends.interest_over_time()

    data = []

    for _, row in interest.iterrows():
        item = [int(row.name.timestamp()), row.values[0]]
        data.append(item)

    return data
