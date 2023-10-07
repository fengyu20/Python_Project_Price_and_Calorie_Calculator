"""
Create a custom Exception called MealTooBigError.
It will raise when an order is over 2000 calories.
"""

class MealTooBigError(Exception):
    """
    The custom exception for big meals.
    """
    