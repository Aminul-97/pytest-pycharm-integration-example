from src.leap_year import check_leap_year
import pytest


def test_database():
    assert check_leap_year(2000) == "Leap Year"
