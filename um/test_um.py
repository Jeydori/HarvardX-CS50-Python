import pytest
from um import count

def test_count():
    assert count("Um um, um um hello um") == 5
    assert count("Hello, um world") == 1
    assert count("Um um, u hello um") == 3
    assert count("Um yum, u hello yummy") == 1

