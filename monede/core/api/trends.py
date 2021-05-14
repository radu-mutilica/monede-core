import logging
from pytrends.request import TrendReq
from cachier import cachier

from monede import settings
from monede.core import db

_pytrends = TrendReq()


def _generate_keywords(name, symbol):
    # primary = sanitize(name)
    # primary = f"{primary} coin" if "coin" not in primary else primary
    secondary = f"{symbol} price"
    # tertiary = f"{symbol} crypto"

    return [secondary]

@cachier(
    stale_after=settings.CACHE_MAX_AGE,
    cache_dir=db.CACHE)
def coin_trend(name, symbol):
    keywords = _generate_keywords(name, symbol)
    logging.debug(f'generated following keywords: {keywords}')
    _pytrends.build_payload(keywords, timeframe='now 1-H')
    interest = _pytrends.interest_over_time()

    data = []

    for _, row in interest.iterrows():
        item = [int(row.name.timestamp() * 1000), sum(row.values)]
        data.append(item)

    return data
