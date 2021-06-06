import logging
from pytrends.request import TrendReq
from cachier import cachier

from monede import settings
from monede.core import db
from monede.core.helpers import sanitize

_pytrends = TrendReq()


def _generate_keywords(name, symbol):
    name = sanitize(name)
    first = f"{name} coin" if "coin" not in name else name
    second = f"{symbol} price"
    third = f"{name} price"
    fourth = f"{symbol} coin"

    return [first, second, third, fourth]

# @cachier(
#     stale_after=settings.CACHE_MAX_AGE,
#     cache_dir=db.CACHE)
def coin_trend(name, symbol, timeframe):
    keywords = _generate_keywords(name, symbol)
    logging.debug(f'generated following keywords: {keywords}')
    _pytrends.build_payload(keywords, timeframe=timeframe)  # 'now 1-H'
    interest = _pytrends.interest_over_time()

    data = []

    for _, row in interest.iterrows():
        item = [int(row.name.timestamp() * 1000), max(row.values)]
        data.append(item)

    return data
