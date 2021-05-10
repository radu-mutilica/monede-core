from monede import settings
from monede.core.api import market


class Monede:
    def __init__(self):
        pass

    @staticmethod
    def all(sort_key=settings.COIN_SORT_KEY):
        return sorted(
            market.coins(vs_currency=settings.VS_CURRENCY), key=lambda x: x[sort_key],
            reverse=True)
