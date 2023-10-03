from meal_counter.data_analysis.order_history import *
import sys
import matplotlib.pyplot as plt
from meal_counter.functions import combo_ids_dict, meal_ids_dict, combo_price_dict, meals_prices_dict


# read from the csv and also convert string to list for future use
order_df = pd.read_csv('./meal_counter/data/order_df.csv', converters={'items': eval})
# create the seperate meal list
meal_list_df = order_df['items'].explode()

# count the values of each meal and sort the value
meal_counts = meal_list_df.value_counts().sort_values(ascending=False)

# create a function that returns the most ordered thing
def most_ordered(type):

    for meal, count in meal_counts.items():
        # print(meal)
        if type == "meal" and meal in meal_ids_dict.values():
            return meal
        elif type == "combo" and meal in combo_ids_dict.values():
            return meal

# Most ordered meals
most_ordered_meal = most_ordered("meal")
# Most ordered combo
most_ordered_combo = most_ordered("combo")

# create a function that returns the combo or meal that brought the most money
combined_prices = {**combo_price_dict, **meals_prices_dict}
# print(combined_prices)

def profitable_meal():
    # conver series to dataframe
    meal_counts_df = meal_counts.reset_index() 
    meal_counts_df.columns = ['items', 'counts']

    # get the price from the dict
    meal_counts_df['prices'] = meal_counts_df['items'].map(lambda x: combined_prices.get(x, 0))

    # calculate the total revenue
    meal_counts_df['total_revenue'] = meal_counts_df['counts'] * meal_counts_df['prices']

    # sort by total revenue
    sorted_df = meal_counts_df.sort_values(by='total_revenue', ascending=False)

    # find the meal name
    max_revenue_meal= sorted_df.iloc[0]['items']

    return max_revenue_meal

most_profitable_meal = profitable_meal()
# print(most_profitable_meal)