"""
Contains functions dedicated to data analysis like calculating:
- most ordered meals
- most ordered combo
- acombo or meal that brought the most money.
"""

import pandas as pd
from meal_counter.functions import (
    combo_ids_dict,
    meal_ids_dict,
    combo_price_dict,
    meals_prices_dict
)

# read from the csv
meal_counts = pd.read_csv('./meal_counter/data/meal_counts.csv')

def most_ordered(meal_type):
    """
    A general function that returns the most ordered thing.
    """
    for _, row in meal_counts.iterrows():
        meal = row['items']

        if meal_type == "meal" and meal in meal_ids_dict.values():
            return meal
        elif meal_type == "combo" and meal in combo_ids_dict.values():
            return meal

def most_ordered_meal():
    """
    A function that returned most ordered meal.
    """
    return most_ordered("meal")

def most_ordered_combo():
    """
    A function that returned most ordered combo.
    """
    return most_ordered("combo")

combined_prices = {**combo_price_dict, **meals_prices_dict}

def profitable_meal():
    """
    A function that returns the combo or meal that is the most profitable one.
    """
    # get the price from the dict
    meal_counts['prices'] = meal_counts['items'].map(lambda x: combined_prices.get(x, 0))

    # calculate the total revenue
    meal_counts['total_revenue'] = meal_counts['count'] * meal_counts['prices']

    # find the meal index by using idxmax
    max_revenue_index = meal_counts['total_revenue'].idxmax()

    # find the meal name
    max_revenue_meal = meal_counts.loc[max_revenue_index, 'items']

    return max_revenue_meal
