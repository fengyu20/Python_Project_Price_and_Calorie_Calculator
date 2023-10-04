"""
Functions to validate the effectiveness of the calorie counter and price counter functions.
"""

import pytest
from meal_counter.functions import calorie_counter, price_counter

meal_combo_list = ["sweet potatoes","vegan combo","cheesy combo"]
meal_list = ["sweet potatoes", "veggie burger"]
wrong_list = ["weet potatoes"]

def main():
    """
    Call the test functions.
    """
    test_price_counter()
    test_calorie_counter()

def test_price_counter():
    """
    A function that tests the price counter.
    """
    assert price_counter(meal_combo_list) == 24
    assert price_counter(meal_list) == 9
    with pytest.raises(KeyError):
        price_counter(wrong_list)


def test_calorie_counter():
    """
    A function that tests the calorie counter.
    """
    assert calorie_counter(meal_combo_list) == 1755
    assert calorie_counter(meal_list) == 630
    with pytest.raises(KeyError):
        calorie_counter(wrong_list)
