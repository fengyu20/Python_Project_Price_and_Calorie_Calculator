
# [0, 1, 2]

calories = {
   'Hamburger': 600,
   'Cheese Burger': 750,
   'Veggie Burger': 400,
   'Vegan Burger': 350,
   'Sweet Potatoes': 230,
   'Salad': 15,
   'Iced Tea': 70,
   'Lemonade': 90,
}


def calories_counter_dict(*args):
    sum = 0
    for arg in args:
        for key in arg.keys():
            sum += arg[key]
    return sum

#print(calories_counter_dict(calories))

meal_list = ['Hamburger','Cheese Burger']
meal_list_1 = ['Lemonade']

def calories_counter(*args):
    sum = 0
    # print(args)
    if isinstance(args[0], list):
        ### attention here
        for meal_list in args:
            # print(meal_list)
            for meal in meal_list:
                # print(meal)
                sum += calories.get(meal, 0)
    else:
        for meal in args:
            sum += calories.get(meal, 0)
    
    return sum

# calories_counter(meal_list)

# print(calories_counter(meal_list,meal_list_1))
# print(calories_counter('Hamburger','Cheese Burger'))

combos = {
    "Cheesy Combo" : ["Cheese Burger", "Sweet Potatoes", "Lemonade"],
    "Veggie Combo" : ["Veggie Burger", "Sweet Potatoes", "Iced Tea"],
    "Vegan Combo" : ["Vegan Burger", "Salad", "Lemonade"],
}

# 'Hamburger','Cheese Burger')
    
def calories_counter_combos(*args):
    sum = 0
    for arg in args:
        if type(arg) == dict:
            for value in arg.values():
                for meal in value:
                    # print(meal)
                    try:
                        sum += calories.get(meal)
                    except Exception as e:
                        print("The meal is not in the list")
        # elif arg in combos.keys():

        elif type(arg) == list:
            for meal in arg:
                try:
                    sum += calories.get(meal)
                except Exception as e:
                    print("The meal is not in the list")
        else:
            sum += calories.get(arg)
    
    return sum



print(calories_counter_combos(combos))
print(calories_counter_combos(meal_list,meal_list_1))
print(calories_counter_combos('Hamburger','Cheese Burger'))
