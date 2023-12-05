import pytest
from .Main import MainClass


def test_get_local_number():
    main_instance = MainClass()
    actual = main_instance.get_local_number()
    expeсted = 14
    assert actual == expeсted, " Something went wrong and get_local_number() from Main.py returned not 14"
    print(" тест 1 выполнен удачно")


def test_get_class_number():
    main_instance = MainClass()
    actual = main_instance.get_class_number()
    expeсted = 45
    assert actual > expeсted, "Something went wrong, and get_class_number() from Main.py returns a number less than 45"
    print(" тест 2 выполнен удачно")


def test_get_class_string():
    main_instance = MainClass()
    actual = main_instance.get_class_string()
    assert "hello" in actual or "Hello" in actual, "Тест не пройден"
    print(" тест 3 выполнен удачно")
