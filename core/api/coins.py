from pycoingecko import CoinGeckoAPI


def all():
    cg = CoinGeckoAPI()
    return cg.get_coins_markets(vs_currency='usd')
