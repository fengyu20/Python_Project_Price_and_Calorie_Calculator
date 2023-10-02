meals = [
    {
        "id": "meal-1",
        "name": "hamburger",
        "calories": 600,
        "price": 5
    },
    {
        "id": "meal-2",
        "name": "cheese burger",
        "calories": 750,
        "price": 7
		},
    {
        "id": "meal-3",
        "name": "veggie burger",
        "calories": 400,
        "price": 6
		},
    {
        "id": "meal-4",
        "name": "vegan burger",
        "calories": 350,
        "price": 6
		},
    {
        "id": "meal-5",
        "name": "sweet potatoes",
        "calories": 230,
        "price": 3
		},
    {
        "id": "meal-6",
        "name": "salad",
        "calories": 15,
        "price": 4
		},
    {
        "id": "meal-7",
        "name": "iced tea",
        "calories": 70,
        "price": 2
		},
    {
        "id": "meal-8",
        "name": "lemonade",
        "calories": 90,
        "price": 2
		}
]

combos = [
    {
        "id": "combo-1",
        "name": "cheesy combo",
        "meals": ["meal-2", "meal-5", "meal-8"],
        "price": 11,
    },
    {
        "id": "combo-2",
        "name": "veggie combo",
        "meals": ["meal-3", "meal-5", "meal-7"],
        "price": 10,
    },
    {
        "id": "combo-3",
        "name": "vegan combo",
        "meals": ["meal-4", "meal-6", "meal-8"],
        "price": 10,
    }
]

# change the list to dict 
meals_calories_dict = {}
meals_prices_dict = {}
meal_ids_dict = {}

combo_price_dict = {}
combo_calories_dict = {}

for meal in meals:
    meal_name = meal["name"]
    meal_calories = meal["calories"]
    meal_price = meal["price"]
    meal_id = meal["id"]

    meals_calories_dict[meal_name] = meal_calories
    meals_prices_dict[meal_name] = meal_price
    meal_ids_dict[meal_id] = meal_name

for combo in combos:
    combo_price_dict[combo["name"]] = combo["price"]
    
for combo in combos:
    combo_meals = combo["meals"]
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



print(calorie_counter(["sweet totatoes","vegan combo"]))