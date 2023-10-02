
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

meal_list_1 = ["Cheese Burger", "Lemonade"]
meal_list_2 = ["Vegan Burger", "Sweet Potatoes", "Iced Tea", "Lemonade"]
 
combos = {
    "Cheesy Combo" : ["Cheese Burger", "Sweet Potatoes", "Lemonade"],
    "Veggie Combo" : ["Veggie Burger", "Sweet Potatoes", "Iced Tea"],
    "Vegan Combo" : ["Vegan Burger", "Salad", "Lemonade"],
}

# 'Hamburger','Cheese Burger')
    
def calories_counter(*orders):
    total_energies = 0 
    for order in orders:
        if type(order) == list:
            for meal in order:
                total_energies += calories.get(meal)
        elif order in combos.keys():
            meal_list = combos.get(order)
            for meal in meal_list:
                total_energies += calories.get(meal)
        else:
            total_energies += calories.get(order)
    
    return total_energies


print(calories_counter("Cheesy Combo",'Hamburger','Cheese Burger'))
print(calories_counter(meal_list_1, 'Hamburger','Cheese Burger'))
print(calories_counter('Hamburger','Cheese Burger'))

print(len(meal_list_1))