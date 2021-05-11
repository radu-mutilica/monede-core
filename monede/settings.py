import datetime

MARKET_API_CALL_STALE_AFTER = datetime.timedelta(seconds=60)
INDIVIDUAL_COIN_MARKET_CALL_STALE_AFTER = datetime.timedelta(seconds=60)
CACHE_DIR_NAME = 'monede.tmp'
VS_CURRENCY = 'usd'
COIN_SORT_KEY = 'price_change_percentage_24h'
COIN_TREND_TIMEFRAME = 'now 1-H'