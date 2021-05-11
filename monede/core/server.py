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

            snapshot = Snapshot(
                id=coin_market['id'],
                name=coin_market['name'],
                vs_currency=settings.VS_CURRENCY,
                from_timestamp=from_timestamp,
                to_timestamp=to_timestamp,
                timeframe=settings.COIN_TREND_TIMEFRAME
            )

            coins.append(
                {
                    'id': snapshot.id,
                    'name': snapshot.name,
                    'historical': snapshot.historical.data
                }
            )

        return coins
