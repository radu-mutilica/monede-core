import time

import mock
import pytest


def test_market_all_coins(client):
    """Simple sanity test for the Market api to make sure we return valid coin data"""

    rv = client.get('/all')
    assert b'bitcoin' in rv.data


# todo: fix this patching to work inside the app
@pytest.mark.skip()
def test_market_call_is_cached(client):
    """Test that the caching functionality works fine"""
    with mock.patch('monede.core.coins.Coins') as mock_coins:
        mock_coins.all.return_value = 'test'
        for i in range(3):
            client.get('/all')
            time.sleep(0.1)

        assert mock_coins.all.call_count == 1
