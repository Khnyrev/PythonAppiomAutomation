import pytest
from .Main import get_local_number

def test_get_local_number():
    actual = get_local_number()
    expeted = 14
    assert actual == expeted, print(" Something went wrong and get_local_number() from Main.py returned not 14")
    print("все Tamam!")


