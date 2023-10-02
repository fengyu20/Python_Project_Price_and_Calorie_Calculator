
import json

with open("data/meals.json") as meal_file:
	meals = json.load(meal_file)

with open("data/combos.json") as combos_file:
    combos = json.load(combos_file)

# change the list to dict 
meals_calories_dict = {}
meals_prices_dict = {}
meal_ids_dict = {}

combo_price_dict = {}
combo_calories_dict = {}

for meal in meals['meals']:
    meal_name = meal["name"]
    meal_calories = meal["calories"]
    meal_price = meal["price"]
    meal_id = meal["id"]

    meals_calories_dict[meal_name] = meal_calories
    meals_prices_dict[meal_name] = meal_price
    meal_ids_dict[meal_id] = meal_name

for combo in combos['combos']:
    
    combo_meals = combo["meals"]
    combo_name = combo["name"]
    combo_price_dict[combo_name] = combo["price"]
    
    combo_calories = 0

    for meal in combo_meals:
        # print(meal)
        if meal in meal_ids_dict:
            meal_name = meal_ids_dict[meal]
            meal_calorie = meals_calories_dict[meal_name]
            combo_calories += meal_calorie

    combo_calories_dict[combo["name"]] = combo_calories

# print(combo_calories_dict)


def price_counter(meal_list):
    total_price = 0
    
    for meal in meal_list:
        # print(meal)
        if meal in meals_prices_dict:
            meal_price = meals_prices_dict[meal]
            total_price += meal_price
        elif meal in combo_price_dict:
            combo_price = combo_price_dict[meal]
            total_price += combo_price
        else: 
            print("Can not find the meal for " + meal)
    return total_price

def calorie_counter(meal_list):
    total_calorie_counter = 0
    
    for meal in meal_list:
        # print(meal)

        if meal in meals_calories_dict:
            meal_calories = meals_calories_dict[meal]
            total_calorie_counter += meal_calories
        elif meal in combo_calories_dict:
            combo_calories = combo_calories_dict[meal]
            total_calorie_counter += combo_calories
        else: 
            print("Can not find the meal for " + meal)
        
    return total_calorie_counter


def calorie_counter_recursion(*args):
    total_calorie_counter = 0
    print(len(args))
    #if len(args) == 1:
  
        
    return 0


calorie_counter_recursion(["sweet totatoes","vegan combo"])