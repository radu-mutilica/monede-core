import binance
import logging

from monede import settings
from monede.core.api import markets
from monede.core.coin import Snapshot


class Monede:
    def __init__(self):
        pass

    @staticmethod
    def get(sort_key=settings.COIN_SORT_KEY):
        coin_markets = sorted(
            markets.coins(vs_currency=settings.VS_CURRENCY), key=lambda x: x[sort_key],
            reverse=True)[:5]  # todo: remove the top 5 from here

        coins = []
        for coin_market in coin_markets:
            try:
                snapshot = Snapshot(
                    symbol=coin_market['symbol'],
                    name=coin_market['name']
                )
            except binance.exceptions.BinanceAPIException as e:
                logging.error(
                    f'failed to get binance data for {coin_market["name"]}: {e}')
            else:
                coins.append(
                    {
                        'historical': snapshot.historical.data,
                        **coin_market
                    }
                )
        return coins
