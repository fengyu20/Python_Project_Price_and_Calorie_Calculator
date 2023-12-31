"""
Contains Order Classes, covering the assignment `Basic7: Use OOP logic to handle orders`.
"""

import datetime
from meal_counter.functions import calorie_counter, price_counter
from meal_counter.custom_exceptions import MealTooBigError

class Order:
    """
    This class represents an order.

    Arguments:
        items (list): A list of item ids.
        date (datetime): The date and time of the order.

    Class attributes:
        counter (int): A counter for the number of orders.

    Attributes:
        order_id (str): A unique identifier for the order.
        order_accepted (bool): Whether or not the order was accepted.
        order_refused_reason (str): The reason the order was refused.
        date (datetime): The date and time of the order.
        items (list): A list of item ids.

    Properties:
        calories (int): The total calories for the order.
        price (int): The total price for the order.
    """
    counter = 0

    def __init__(self, items):
        Order.counter += 1
        self._order_id = str(Order.counter)
        self._order_accepted = False
        self._order_refused_reason = ""
        self._date = datetime.datetime.now()
        self._items = items
        self.calories_check()

    def calories_check(self):
        """
        A function that checks should the store accept the order or not.
        """
        try:
            total_calories = calorie_counter(self._items)
            if total_calories > 2000:
                raise MealTooBigError("Total calories exceeds 2000")
            self._order_accepted = True
        except MealTooBigError as big_meal_error:
            self._order_refused_reason = str(big_meal_error)
        except KeyError as not_found_error:
            self._order_refused_reason = str(not_found_error)

    @property
    def calories(self):
        """
        Define a property by calling calorie_counter.
        """
        return calorie_counter(self._items)

    @property
    def price(self):
        """
        Define a property by calling price_counter.
        """
        return price_counter(self._items)
    def get_order_id(self):
        """
        Returns the order ID.
        """
        return self._order_id

    def get_order_accepted(self):
        """
        Returns whether the order was accepted.
        """
        return self._order_accepted

    def get_order_refused_reason(self):
        """
        If the order is refused, returns the reason the order was refused.
        """
        return self._order_refused_reason

    def get_date(self):
        """
        Returns the date and time of the order.
        """
        return self._date

    def get_items(self):
        """
        Returns the list of item IDs.
        """
        return self._items
