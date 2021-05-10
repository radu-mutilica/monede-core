import pytest

import monede


@pytest.fixture
def client():
    monede.app.config['TESTING'] = True

    with monede.app.test_client() as client:
        yield client
