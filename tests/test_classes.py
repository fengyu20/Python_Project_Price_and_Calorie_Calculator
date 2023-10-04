"""
Functions to test the Class implementations.
"""

import datetime
from meal_counter.classes import Order

meal_combo_list = ["sweet potatoes","vegan combo","cheesy combo"]
big_meal_list = ["sweet potatoes", "veggie burger","vegan combo","cheesy combo"]
wrong_list = ["weet potatoes"]

def main():
    """
    Call the test functions.
    """
    test_init()
    test_calroies_check()
    test_properties()

def test_init():
    """
    A function that checks the type of attributes.
    """
    # check the class attributes
    assert type(Order.counter) == int

    # check the type of attributes
    order = Order(meal_combo_list)
    assert type(order._order_id) == str
    assert type(order._order_accepted) == bool
    assert type(order._order_refused_reason) == str
    assert isinstance(order._date, datetime.datetime)
    assert type(order._items) == list

def test_calroies_check():
    """
    A function that validates the order is accepted or not.
    """    
    normal_order = Order(meal_combo_list)
    assert normal_order._order_accepted

    wrong_order = Order(wrong_list)
    assert not wrong_order._order_accepted
    assert wrong_order._order_refused_reason == "'Cannot find the meal for weet potatoes'"

    big_order = Order(big_meal_list)
    assert not big_order._order_accepted
    assert big_order._order_refused_reason == "Total calories exceeds 2000"  


def test_properties():
    """
    A function that validates properties.
    """
    order = Order(meal_combo_list)
    assert order.calories == 1755
    assert order.price == 24

