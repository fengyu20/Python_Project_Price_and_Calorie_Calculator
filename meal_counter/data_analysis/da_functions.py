from meal_counter.data_analysis.order_history import *
import sys
import matplotlib.pyplot as plt
from meal_counter.functions import combo_ids_dict, meal_ids_dict, combo_price_dict, meals_prices_dict


# read from the csv
meal_counts = pd.read_csv('./meal_counter/data/meal_counts.csv')

# print(meal_counts.head(10))

# create a function that returns the most ordered thing
def most_ordered(type):

    for index, row in meal_counts.iterrows():
        meal = row['items']

        if type == "meal" and meal in meal_ids_dict.values():
            return meal
        elif type == "combo" and meal in combo_ids_dict.values():
            return meal

# Most ordered meals
def most_ordered_meal():
    return most_ordered("meal")

# Most ordered combo
def most_ordered_combo():
    return most_ordered("combo")

# create a function that returns the combo or meal that brought the most money
combined_prices = {**combo_price_dict, **meals_prices_dict}
# print(combined_prices)

def profitable_meal():

    # get the price from the dict
    meal_counts['prices'] = meal_counts['items'].map(lambda x: combined_prices.get(x, 0))

    # calculate the total revenue
    meal_counts['total_revenue'] = meal_counts['count'] * meal_counts['prices']

    # find the meal index by using idxmax
    max_revenue_index = meal_counts['total_revenue'].idxmax()

    # find the meal name
    max_revenue_meal = meal_counts.loc[max_revenue_index, 'items']

    return max_revenue_meal

