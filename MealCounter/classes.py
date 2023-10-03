from MealCounter.functions import calorie_counter, price_counter
import datetime
import sys

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

    def __init__(self, items, date=None):
        Order.counter += 1
        self._order_id = str(Order.counter)
        self._order_accepted = False
        self._order_refused_reason = ""
        self._date = datetime.datetime.now() 
        self._items = items
        self.calories_check()

    def calories_check(self):
        try:
            total_calories = calorie_counter(self._items)
            if total_calories > 2000:
                self._order_refused_reason = "Total calories exceeds 2000"
            else:
                self._order_accepted = True
        except KeyError as e:
            self._order_refused_reason = str(e)
            

    @property
    def calories(self):
        return calorie_counter(self._items)

    @property
    def price(self):
        return price_counter(self._items)
    

order = Order(["sweet potatoes","vegan combo","cheesy combo"])
#order.calories
#print(order.calories)
order.calories_check()
print(order._order_id)
print(order.price)