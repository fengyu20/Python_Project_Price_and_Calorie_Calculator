from order_history import *
import sys
import matplotlib.pyplot as plt

# read from the csv and also convert string to list for future use
order_df = pd.read_csv('./MealCounter/data/order_df.csv', converters={'items': eval})

# calculate the price and calories of each day for the accepted orders
daily_sums = order_df[order_df['order_accepted'] == True].groupby('date')[['price', 'calories']].sum().reset_index()

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

# create the seperate meal list
meal_list_df = order_df['items'].explode()
# count the values
meal_counts = meal_list_df.value_counts()

print(meal_counts)