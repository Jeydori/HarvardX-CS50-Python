import pytest

from plates import is_valid

def test_valid_plate():
    assert is_valid("AB123")

def test_too_short():
    assert is_valid("A") == False

def test_special_characters():
    assert is_valid("AB@123") == False

def test_leading_zero():
    assert is_valid("AB0123") == False

def test_leading_alphabet():
    assert is_valid("A40123") == False

def test_digits_at_end():
    assert is_valid("ABB22C") == False

