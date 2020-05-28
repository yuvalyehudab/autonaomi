#test_saver
import pytest

from autonaomi.saver import Saver

_DATABASE_URL = 'mongodb://127.0.0.1:3306'

@pytest.fixture
def get_saver():
    return Saver(_DATABASE_URL)

def test_create(get_saver):
    assert get_saver.database_url == _DATABASE_URL
    assert Saver(_DATABASE_URL).database_url == _DATABASE_URL
'''
def test_save(get_saver):
    data = '123123'
    get_saver.save('pose', data)
    assert 1 == 1
'''