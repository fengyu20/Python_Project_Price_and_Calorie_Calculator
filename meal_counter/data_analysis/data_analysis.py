from order_history import *
import sys
import matplotlib.pyplot as plt
from meal_counter.functions import combo_ids_dict, meal_ids_dict


# read from the csv and also convert string to list for future use
order_df = pd.read_csv('./MealCounter/data/order_df.csv', converters={'items': eval})

# calculate the price and calories of each day for the accepted orders
# daily_sums = order_df[order_df['order_accepted'] == True].groupby('date')[['price', 'calories']].sum().reset_index()

""" # create a plot to show "Total calories per day"
plt.plot(daily_sums['date'], daily_sums['calories'], label='Total Calories')
plt.title('Daily Sum of Calories')
plt.xlabel('Date')
plt.ylabel('Calories')
plt.legend()
plt.show()

# create a plot to show "Total price per day"
plt.plot(daily_sums['date'], daily_sums['price'], label='Total Price')
plt.title('Daily Sum of Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show() """

# create a function that returns the most ordered thing
def most_ordered():
    # create the seperate meal list
    meal_list_df = order_df['items'].explode()
    # count the values of each meal
    meal_counts = meal_list_df.value_counts()
    # sort the value
    meal_counts = meal_counts.sort_values(ascending=False)
    # get the maxmized meal

    return meal_counts

# create a function that returns the most ordered meal

def most_ordered_meal():
    meal_df = most_ordered()
    #print(meal_df)
    for meal in meal_df.items():
        print(meal)
        if meal in meal_ids_dict.values():
            return meal
        
print(most_ordered_meal())

# create a function that returns the most ordered combo
def most_ordered_combo():
    meal_df = most_ordered()
    #print(meal_df)
    for meal in meal_df.items():
        if meal in combo_ids_dict.values():
            return meal
        
print(most_ordered_combo())