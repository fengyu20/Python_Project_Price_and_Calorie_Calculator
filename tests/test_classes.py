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
    test_calories_check()
    test_properties()

def test_init():
    """
    A function that checks the type of attributes.
    """
    # check the class attributes
    assert isinstance(Order.counter, int)

    # check the type of attributes
    order = Order(meal_combo_list)
    assert isinstance(order.get_order_id(), str)
    assert isinstance(order.get_order_accepted(), bool)
    assert isinstance(order.get_order_refused_reason(), str)
    assert isinstance(order.get_date(), datetime.datetime)
    assert isinstance(order.get_items(), list)


def test_calories_check():
    """
    A function that validates the order is accepted or not.
    """

    normal_order = Order(meal_combo_list)
    assert normal_order.get_order_accepted()

    wrong_order = Order(wrong_list)
    assert not wrong_order.get_order_accepted()
    assert wrong_order.get_order_refused_reason() == "'Cannot find the meal for weet potatoes'"

    big_order = Order(big_meal_list)
    assert not big_order.get_order_accepted()
    assert big_order.get_order_refused_reason() == "Total calories exceeds 2000"


def test_properties():
    """
    A function that validates properties.
    """
    order = Order(meal_combo_list)
    assert order.calories == 1755
    assert order.price == 24
