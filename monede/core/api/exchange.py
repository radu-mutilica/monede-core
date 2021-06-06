import os
from cachier import cachier

from binance import Client
from pycoingecko import CoinGeckoAPI
from monede import settings
from monede.core import db

_cg = CoinGeckoAPI()
_bin = client = Client(
    os.environ['BINANCE_API_KEY'],
    os.environ['BINANCE_API_SECRET']
)

# @cachier(
#     stale_after=settings.CACHE_MAX_AGE,
#     cache_dir=db.CACHE)
def coin_markets(vs_currency):
    return _cg.get_coins_markets(vs_currency=vs_currency)

# @cachier(
#     stale_after=settings.CACHE_MAX_AGE,
#     cache_dir=db.CACHE)
def coin_history(symbol, timeframe):
    history = client.get_historical_klines(
        f'{symbol.upper()}USDT',
        Client.KLINE_INTERVAL_1MINUTE,
        timeframe)

    return history


def coin_stats(symbol):
    return _cg.get_coin_by_id(
        symbol,
        localization=False,
        market_data=True,
        community_data=False,
        developer_data=False,
        sparkline=False,
        vs_currencies='usd'
    )
