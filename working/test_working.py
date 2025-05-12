import pytest
from working import convert

def test_conversion():
    assert convert("9 AM to 5 PM") == f"09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == f"09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == f"10:00 to 20:50"

def test_exception():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
