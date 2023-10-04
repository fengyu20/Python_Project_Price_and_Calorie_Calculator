import pytest
from meal_counter.data_analysis.da_functions import *

def main():
    test_most_ordered_meal()
    test_most_ordered_combo()
    test_profitable_meal()

def test_most_ordered_meal():
    assert most_ordered_meal() == "vegan burger"

def test_most_ordered_combo():
    assert most_ordered_combo() == "veggie combo"

def test_profitable_meal():
    assert profitable_meal() == "cheesy combo"