import sys
import json
import argparse

# load json files
def load_json(file_path):
    with open(file_path) as f:
        return json.load(f)

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

# create a counter function
def general_counter(meal_list, dict_type):
    total_value = 0
    
    for meal in meal_list:
        if meal in dict_type:
            total_value += dict_type[meal]
        else: 
            raise KeyError(f"Cannot find the meal for {meal}")
    
    return total_value

# create price counter function, the argument is a list of meals 
def price_counter(meal_list):
    combined_price_dict = {**meals_prices_dict, **combo_price_dict}

    return general_counter(meal_list, combined_price_dict)

# create calorie counter function, the argument is a list of meals 
def calorie_counter(meal_list):
    combined_calories_dict = {**meals_calories_dict, **combo_calories_dict}

    return general_counter(meal_list, combined_calories_dict)

def main():
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