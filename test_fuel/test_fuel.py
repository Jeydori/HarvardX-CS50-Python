import pytest

from fuel import convert, gauge

def test_convert():
    assert convert("4/5") == 80
    assert convert("1/100") == 1
    assert convert("99/100") == 99

def test_gauge():
    assert gauge(80) == "80%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"

def test_exceptions():
    with pytest.raises(ZeroDivisionError):
        convert("101/0")

    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("101/100")
