## 1. Intro: A Brief Explanation of This Repository
This repository helps users in calculating the price and calories of a meal list. It can also be used by stores to track and analyse their orders.

* This repository is also the final project for the Python classes, covering the assignment `Basic9: Create a repository on GitHub and push your work`.

## 2. Before You Start: How to Clone the Repository and Setup the Environment

### 2.1 Clone and Setup

1. **Clone the Repository**:
Use `git clone https://github.com/fengyu20/AIRE_Python.git` to clone the Repository.

2. **Setup Environment**
   - **Create the Virtual Environment**:
     - If you haven't installed `virtualenv`, please run `pip install virtualenv` first.
     - Create the virtual environment using `virtualenv the_name_of_your_virtual_env`.
     - Activate the virtual environment using `source the_name_of_your_virtual_env/bin/activate`(For Mac Users).
     - To exit the virtual environment, use `deactivate`.
   - **Install Dependencies**:
     - Dependencies are listed in `requirements.txt`. Install them using `pip install -r requirements.txt`.

## 3. Step by Step Guide:

### 3.1 Details About the Code Contained in the Repository
- **meal_counter**: A directory used to store functions and data.
    - **data**: A directory containing the JSON files for meals, combos, and orders, and CSV files for DataFrame.
    - **data_analysis**: A directory including data analysis contents, covering the assignment `Advanced7: Use data analysis libraries`.
        - `__init__.py`: Essential for importing functions from other files within the package.
        - `order_history.py`: Organizes data from JSON files and saves DataFrames to CSV for future use.
        - `da_functions.py`: Contains functions dedicated to data analysis like calculating most ordered meals, most ordered combo, and combo or meal that brought the most money.
    - `__init__.py`: Essential for importing functions from other files within the package.
    - `classes.py`: Contains Order Classes, covering the assignment `Basic7: Use OOP logic to handle orders`.
    - `custom_exceptions.py`: Defines MealTooBigError, covering the assignment `Advanced4: Create exceptions`.
    - `functions.py`: Incorporates calorie and price counter functions, covering assignments such as `Basic1: Create a calorie counter function`, `Basic2: Handle combos`, `Basic3: Handle errors`, `Basic4: Use more complex data`, `Basic5: Create a price counter function`, `Basic6: Store your data in JSON files` and `Advanced3: Use a recursive function`.
- **tests**: A directory dedicated to test scripts, vcvering assignments of `Advanced6: Add unit tests` but using `pytest` as it's more familiar for me.
    - `__init__.py`: Essential for importing functions from other files within the package.
    - `test_functions.py`: Functions to validate the effectiveness of the calorie counter and price counter functions.
    - `test_classes.py`: Functions to test the Class implementations.
    - `test_da_functions.py`: Functions to validate the data analysis functions.
- `main.ipynb`: Contains all the functions.
- `requirements.txt`: Dependencies that need to be installed, covering the assignment `Advanced1: Create a virtual environment and document your requirements`.
- `README.md`: File that introduce this repo, covering the assignment `Advanced5: Add a README file`.

### 3.2 How to Use It
- If you want to interact with the entire project, navigate to the root folder and open `main.ipynb`. Execute the relevant code blocks to see the results, and feel free to modify them as needed.
    - `1. Functions`: Utilize the calorie and price counter functions in this part.
    - `2. Classes`: Submit the order to check their total price, total calories, and acceptance status etc.
    - `3. Data Analysis`: Delve into the order data for a comprehensive understanding.
    - `4. Plot`: Generate plots of total calories per day, total earnings per day, and average earnings by customer served per day.
    - `5. Run the Test Functions`: Ensure that the functions and classes work correctly.
    - `6. Additional Info`: Verify whether the repository adheres to PEP8 standards or not.
- If you have a meal list and want to know the price or the calories and want to interact with the command line:
    - Navigate to the root folder, and run the following command:
        - `python3 meal_counter/functions.py -f {function_name} -m "meal1" "meal2" ...`
        - `-f {function_name}`: Specify the function to use (price_counter or calorie_counter).
        - `-m`: List your meals following the format `"meal1" "meal2"`.
    - **Example**:
        - `python3 meal_counter/functions.py -f price_counter -m "sweet potatoes" "vegan combo" "cheesy combo"`
        - The output should be `Total price: 24`

## 4. Test the Code: How to Run Tests
- Ensure you are in the root folder. Run the following commands:
    ```bash
    # To test functions.py
    pytest tests/test_functions.py  
    # To test classes.py
    pytest tests/test_classes.py  
    # To test da_functions.py  
    pytest tests/test_da_functions.py    
    ```
- **Note**: These test scripts include functions to handle normal and edge cases. Feel free to modify them to meet your needs.

## 5. Additional Info
- This repo respects PEP 8(covering the assignment `Advanced2: Respect PEP 8`.), after installing `pylint`, you can run `pylint **/*.py` in the root folder.
- The output should be `Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)`.