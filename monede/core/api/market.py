from cachier import cachier
from pycoingecko import CoinGeckoAPI

from monede import settings
from monede.core import db

_cg = CoinGeckoAPI()

# cache the results of this API call
@cachier(
    stale_after=settings.MARKET_API_CALL_STALE_AFTER,
    cache_dir=db.CACHE)
def coins(vs_currency):
    return _cg.get_coins_markets(vs_currency=vs_currency)
