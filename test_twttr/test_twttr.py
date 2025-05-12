import pytest

from twttr import shorten

def test_shorten():
    assert shorten("abacada") == "bcd"
    assert shorten("Twitter") == "Twttr"
    assert shorten("AEIOUaeiou") == ""
    assert shorten("12345") == "12345"
    assert shorten("Hello, World!") == "Hll, Wrld!"

