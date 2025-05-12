import pytest
from seasons import convertToMinutes

def test_valid_date():
    obj = convertToMinutes("2000-01-01")
    result = str(obj)
    assert "minutes" in result
    assert result[0].isupper()

def test_invalid_format():
    with pytest.raises(SystemExit):
        convertToMinutes("01-01-2000").__str__()

def test_non_date_string():
    with pytest.raises(SystemExit):
        convertToMinutes("hello world").__str__()

