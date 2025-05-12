import pytest

from bank import value

def test_value_0():
    assert value("hello") == 0
    assert value("hello, sir") == 0
    assert value("HeLLo") == 0
    assert value("HELLO, sir") == 0

def test_value_20():
    assert value("hi") == 20
    assert value("hI") == 20

def test_value_100():
    assert value("good morning") == 100
    assert value("nice morning") == 100
    assert value("GOOD MORNING") == 100
    assert value("nIcE mOrning") == 100

