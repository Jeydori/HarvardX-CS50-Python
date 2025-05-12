import pytest

from numb3rs import validate

def test_numb3rs():
    assert validate("13.245.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True
    assert validate("275.255.255.255") == False
    assert validate("1.15.4.1000") == False
    assert validate("127.300.1.2") == False
