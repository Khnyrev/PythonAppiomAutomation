import pytest
from .Main import MainClass


def test_get_local_number():
    main_instance = MainClass()
    actual = main_instance.get_local_number()
    expeted = 14
    assert actual == expeted, " Something went wrong and get_local_number() from Main.py returned not 14"
    print(" все Tamam!")


def test_get_class_number():
    main_instance = MainClass()
    actual = main_instance.get_class_number()
    print(f"actual = {actual}")
    expeted = 45
    assert actual > expeted, "Something went wrong, and get_class_number() from Main.py returns a number less than 45"
    print(" все Tamam!")
