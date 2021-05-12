import logging

from cryptowatch_client import Client
# from cachier import cachier
from pycoingecko import CoinGeckoAPI

# from monede import settings
# from monede.core import db

_cg = CoinGeckoAPI()
_cw = Client(timeout=30)


# cache the results of this API call
# @cachier(
#     stale_after=settings.MARKET_API_CALL_STALE_AFTER,
#     cache_dir=db.CACHE)
def coins(vs_currency):
    return _cg.get_coins_markets(vs_currency=vs_currency)


# @cachier(
#     stale_after=settings.INDIVIDUAL_COIN_MARKET_CALL_STALE_AFTER,
#     cache_dir=db.CACHE)
def cg_coin_history(symbol, vs_currency, from_timestamp, to_timestamp):
    history = _cg.get_coin_market_chart_range_by_id(
        symbol=symbol,
        vs_currency=vs_currency,
        from_timestamp=from_timestamp,
        to_timestamp=to_timestamp
    )
    logging.debug(history)
    return history


def cw_coin_history(symbol, vs_currency, from_timestamp, to_timestamp):
    pair = f'{symbol.lower()}usd'
    history = _cw.get_markets_ohlc(
        exchange='gdax',
        pair=pair,
        before=to_timestamp,
        after=from_timestamp,
        periods='60').json()['result']['60']
    return history


coin_history = cw_coin_history
