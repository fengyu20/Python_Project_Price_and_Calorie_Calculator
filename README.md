
## 1. Intro: A brief explanation of this repository
This repository could help users to calculate the price and calories of the meal list.
It also could be used for stores to track the order, for example, reject the non-existed order.


## 2. Before Start: How to clone the repository and setup the environment

1. Clone
2. Setup
2.1 create the virtual environment
2.2 install the dependencies
- In this repository, we use `pytest` to test c0de. You need to use `pip install pytest` to install it in advance.
- In the 

## 3. Step by step guide:
### 3.1 Details about the code contained in the repository
- `MealCounter`: A directory used to store functions and data.
    - `__init__.py`: This file is essential when importing functions from other files within the package.
    - `classes.py`: Contains Order Classes, covering the assignment of `Use OOP logic to handle orders`.
    - `data`: A directory containing the json files for meals, combos, and orders.
    - `exceptions.py`: Defines custom exception classes utilized within the project.
    - `functions.py`: Incorporates calorie and price counter functions, covering assignments such as `Create a calorie counter function`, `Handle combos`, `Handle errors`, `Use more complex data`, `Create a price counter function`, and `Store your data in json files`.
- `tests`: A directory dedicated to test scripts and files, which include unit tests and fixtures.
    - `__init__.py`: This file is essential when importing functions from other files within the package.
    - `test_functions.py`: Functions to validate the effectiveness of the calorie counter and price counter functions.
    - `test_classes.py`: Functions to test the Class implementationå.


### 3.2 How to use it
- If you have a meal list, and want to know the price or the calories. 
    - Navigate to the root folder, and run the following command:
        - `python3 MealCounter/functions.py -f {function_name} -m "meal1" "meal2" ...`
        - `-f {function_name}`: Specify the function to use (price_counter or calorie_counter).
        - `-m`: List your meals follwoing the format as `"meal1" "meal2"`
    - Example:
        - `python3 MealCounter/functions.py -f price_counter -m "sweet potatoes" "vegan combo" "cheesy combo"`
        - The output should be `Total price: 24`

## 4. Test the code: How to run tests

- Be sure you are at the root folder. Run the following command:
```
pytest tests/test_functions.py  # To test functions.py
pytest tests/test_classes.py    # To test classes.py

```
- Note: These test scripts include functions to handle edge cases. Feel free to modify them to meet your needs.