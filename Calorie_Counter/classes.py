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
        pass

    @property
    def calories(self):
        return self._calories

    @property
    def price(self):
        return self._price