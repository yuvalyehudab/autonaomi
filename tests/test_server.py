#test_server.py
import pytest

from autonaomi.server import run_server

_HOST_1 = '127.0.0.1'
_PORT_1 = 8000

def print_message(message):
    print(message)

def test_no_error(capsys):
    assert 1
