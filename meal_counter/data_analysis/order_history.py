"""
Organizes data from JSON files and saves DataFrames to CSV for future use.
"""

import pandas as pd
from meal_counter.functions import load_json, combo_ids_dict, meal_ids_dict
from meal_counter.classes import Order

def main():
    """
    Create CSV files to store the dataframes for future data analysis,
    """
    # save the df to csv for creating plots
    order = create_order_df()
    order.to_csv('./meal_counter/data/order_df.csv', index=False)

    # create the seperate meal list
    meal_list_df = order['items'].explode()
    meal_counts = meal_list_df.value_counts().sort_values(ascending=False)

    # save it to the csv for future use
    meal_counts.to_csv('./meal_counter/data/meal_counts.csv', index=True)

def create_order_df():
    """
    A function that create the dataframe from the json file.
    """
    # create the dataframe from the json file
    orders = load_json("./meal_counter/data/orders_history.json")
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

def id_name_finder(meal_ids):
    """
    A function that takes meal_id as arguments and return names
    """
    meal_names = []

    for meal_id in meal_ids:
        if meal_id in meal_ids_dict:
            meal_names.append(meal_ids_dict[meal_id])
        elif meal_id in combo_ids_dict:
            meal_names.append(combo_ids_dict[meal_id])
        else:
            raise KeyError(f"Cannot find the meal for {meal_id}")
    return meal_names

def get_order_attributes(row):
    """
    A function that takes meal names as arguments and return atrributes as columns in the dataframe.
    """
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
