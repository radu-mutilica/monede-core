import datetime

from monede import settings
from monede.core.api import exchange
from monede.core.coin import Snapshot
from monede.core.helpers import Timeframe


def top(sort_key=settings.COIN_SORT_KEY):
    coin_markets = sorted(
        exchange.coin_markets(vs_currency=settings.VS_CURRENCY), key=lambda x: x[sort_key],
        reverse=True)[:25]  # todo: remove the limit from here

    return coin_markets


def coin_market(symbol):
    return exchange.coin_stats(symbol)['market_data']


def coin_history(symbol, timeframe=4):
    coin_stats = exchange.coin_stats(symbol)

    snapshot = Snapshot(
        symbol=symbol,
        name=coin_stats['name'],
        timeframe=Timeframe(timeframe)
    )

    return {
        'historical': snapshot.historical.data,
        'change': {
            'hours_timeframe': timeframe,
            'amount': snapshot.historical.change_amount,
            'percentage': snapshot.historical.change_percentage
        },
        **coin_stats['market_data']
    }


def latest_example():
    # todo: properly implement this (just a placeholder atm)
    return {
        'growth': {
            'notification': int((datetime.datetime.now() - datetime.timedelta(hours=2)).timestamp()) // 60 * 60 * 1000,
            'peak': int((datetime.datetime.now() - datetime.timedelta(hours=1)).timestamp()) // 60 * 60 * 1000,
        },
        **coin_history('aave')
    }
