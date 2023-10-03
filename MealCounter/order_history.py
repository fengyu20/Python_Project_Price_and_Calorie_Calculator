from functions import calorie_counter, price_counter, load_json, combo_ids_dict, meal_ids_dict
import pandas as pd
from classes import *


def main():
    # save the df to csv for future
    order = create_order_df()
    order.to_csv('./MealCounter/data/order_df.csv', index=False) 

# get the dataframe from the json file
def create_order_df():
    # create the dataframe from the json file
    orders = load_json("./MealCounter/data/orders_history.json")
    order_list = orders['orders']
    order_df = pd.DataFrame(order_list, columns = ['items','date'] )

    # covert date to datetime
    order_df['date'] = pd.to_datetime(order_df['date'], format='%d-%b-%Y')

    # convert meal ids to meal names
    order_df['items'] = order_df['items'].apply(id_name_finder)

    # add more attributes from Class order by creating a new df
    attributes_df = order_df.apply(get_order_attributes, axis = 1)

    # update attributes df to the exisiting df
    order_df = pd.concat([order_df, attributes_df], axis = 1)

    return order_df
    



# create a function that takes meal_id as argumetns and return names
def id_name_finder(meal_ids):
    meal_names = []

    for meal_id in meal_ids:
        if meal_id in meal_ids_dict:
            meal_names.append(meal_ids_dict[meal_id])
        elif meal_id in combo_ids_dict:
            meal_names.append(combo_ids_dict[meal_id])
        else:
            raise KeyError(f"Cannot find the meal for {meal_id}")
    
    return meal_names

# create a function that takes meal names as arguments and return atrributes in pd

def get_order_attributes(row):
    order = Order(items=row['items']) 
    return pd.Series({
        'order_id': order._order_id,
        'order_accepted': order._order_accepted,
        'order_refused_reason': order._order_refused_reason,
        'calories': order.calories,
        'price': order.price
    })


if __name__ == "__main__":
    main()