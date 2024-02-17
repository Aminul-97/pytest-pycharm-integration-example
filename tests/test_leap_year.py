from src.leap_year import check_leap_year
import pytest


def test_leap_year():
    assert check_leap_year(2000) == "Leap Year"

def test_not_leap_year():
    assert check_leap_year(2001) == "Not Leap Year"
