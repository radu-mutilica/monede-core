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
                        'symbol': snapshot.symbol,
                        'name': snapshot.name,
                        'historical': snapshot.historical.data,
                        'price_change_percentage_24h': coin_market['price_change_percentage_24h'],
                        'total_volume': coin_market['total_volume'],
                        'current_price': coin_market['current_price'],
                        'image': coin_market['image'],
                        'ath': coin_market['ath'],
                        'ath_change_percentage': coin_market['ath_change_percentage'],
                        'market_cap': coin_market['market_cap'],
                        'market_cap_rank': coin_market['market_cap_rank']
                    }
                )
        return coins
