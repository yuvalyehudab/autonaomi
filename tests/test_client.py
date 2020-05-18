#test_client.py
import pytest

#from autonaomi import client
from autonaomi.client import upload_sample

_HOST_1 = '127.0.0.1'
_PORT_1 = 8000
_PATH_1 = 'sample1.mind.gz'

def test_no_error(capsys):
    upload_sample(host=_HOST_1, port=_PORT_1, path=_PATH_1)
    out, err = capsys.readouterr()
    assert err == ''
