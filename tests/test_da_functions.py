"""
Functions to validate the data analysis functions.
"""

from meal_counter.data_analysis.da_functions import (
    most_ordered_meal,
    most_ordered_combo,
    profitable_meal
)

def main():
    """
    Call the test functions.
    """
    test_most_ordered_meal()
    test_most_ordered_combo()
    test_profitable_meal()

def test_most_ordered_meal():
    """
    Validate the most_ordered_meal
    """
    assert most_ordered_meal() == "vegan burger"

def test_most_ordered_combo():
    """
    Validate the most_ordered_combo
    """
    assert most_ordered_combo() == "veggie combo"

def test_profitable_meal():
    """
    Validate the most profitable_meal
    """
    assert profitable_meal() == "cheesy combo"
