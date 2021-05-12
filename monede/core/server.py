import logging

from monede import settings
from monede.core.api import markets
from monede.core.coin import Snapshot
from monede.core.helpers import get_snapshot_timestamps


class Monede:
    def __init__(self):
        pass

    @staticmethod
    def get(sort_key=settings.COIN_SORT_KEY):
        coin_markets = sorted(
            markets.coins(vs_currency=settings.VS_CURRENCY), key=lambda x: x[sort_key],
            reverse=True)[:2]  # todo: remove the top 5 from here

        from_timestamp, to_timestamp = get_snapshot_timestamps()

        coins = []
        for coin_market in coin_markets:
            try:
                snapshot = Snapshot(
                    symbol=coin_market['symbol'],
                    name=coin_market['name'],
                    vs_currency=settings.VS_CURRENCY,
                    from_timestamp=from_timestamp,
                    to_timestamp=to_timestamp,
                    timeframe=settings.COIN_TREND_TIMEFRAME
                )
            except Exception:
                logging.exception(
                    f'failed to create coin snapshot for {coin_market["name"]}:')
            else:
                coins.append(
                    {
                        'symbol': snapshot.symbol,
                        'name': snapshot.name,
                        'historical': snapshot.historical.data
                    }
                )
        return coins
