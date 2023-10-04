"""
Incorporates calorie and price counter functions, covering assignments such as 
- `Basic1: Create a calorie counter function`
- `Basic2: Handle combos`, `Basic3: Handle errors`
- `Basic4: Use more complex data`
- `Basic5: Create a price counter function`
- `Basic6: Store your data in JSON files`.
"""

import json
import argparse

def load_json(file_path):
    """
    A function that could load json files.
    """
    with open(file_path, encoding='utf-8') as json_file:
        return json.load(json_file)

meals = load_json("./meal_counter/data/meals.json")
combos = load_json("./meal_counter/data/combos.json")

meals_calories_dict = {}
meals_prices_dict = {}
meal_ids_dict = {}

# create empty dics to track the meal dicts
# including: calories, prices and the relationship between meal_id and name

for meal in meals['meals']:
    meal_name, meal_calories, meal_price, meal_id = meal["name"], meal["calories"], meal["price"], meal["id"]

    meals_calories_dict[meal_name] = meal_calories
    meals_prices_dict[meal_name] = meal_price
    meal_ids_dict[meal_id] = meal_name


# create dics to track the combo dicts, including calories and prices
combo_price_dict = {}
combo_calories_dict = {}
combo_ids_dict = {}

for combo in combos['combos']:
    combo_meals = combo["meals"]
    combo_name = combo["name"]
    combo_id = combo["id"]


    combo_price_dict[combo_name] = combo["price"]
    combo_ids_dict[combo_id] = combo_name

    combo_calories = 0

    for meal in combo_meals:
        if meal in meal_ids_dict:
            meal_name = meal_ids_dict[meal]
            meal_calorie = meals_calories_dict[meal_name]
            combo_calories += meal_calorie

    combo_calories_dict[combo["name"]] = combo_calories

def general_counter(meal_list, dict_type):
    """
    A general counter function.
    """
    total_value = 0

    for meal in meal_list:
        if meal in dict_type:
            total_value += dict_type[meal]
        else:
            raise KeyError(f"Cannot find the meal for {meal}")
       
    return total_value

def price_counter(meal_list):
    """
    A price counter function, the argument is a list of meals 
    """
    combined_price_dict = {**meals_prices_dict, **combo_price_dict}

    return general_counter(meal_list, combined_price_dict)

def calorie_counter(meal_list):
    """
    A calorie counter function, the argument is a list of meals.
    """
    combined_calories_dict = {**meals_calories_dict, **combo_calories_dict}

    return general_counter(meal_list, combined_calories_dict)

def main():
    """
    A function that allows user to interact with the function.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--function', choices=['price_counter', 'calorie_counter'])
    parser.add_argument('-m', '--meals', nargs='+')

    args = parser.parse_args()

    if args.function == 'price_counter':
        total_price = price_counter(args.meals)
        print(f'Total price: {total_price}')
    elif args.function == 'calorie_counter':
        total_calories = calorie_counter(args.meals)
        print(f'Total calories: {total_calories} kcal')

if __name__ == "__main__":
    main()