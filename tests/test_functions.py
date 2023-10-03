import pytest
from meal_counter.functions import *

meal_combo_list = ["sweet potatoes","vegan combo","cheesy combo"]
meal_list = ["sweet potatoes", "veggie burger"]
wrong_list = ["weet potatoes"]

def main():
    test_price_counter()
    test_calorie_counter()

def test_price_counter():
    assert price_counter(meal_combo_list) == 24
    assert price_counter(meal_list) == 9
    with pytest.raises(KeyError):
        price_counter(wrong_list) 


def test_calorie_counter():
    assert calorie_counter(meal_combo_list) == 1755
    assert calorie_counter(meal_list) == 630
    with pytest.raises(KeyError):
        calorie_counter(wrong_list) 
