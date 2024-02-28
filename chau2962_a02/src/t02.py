"""
-------------------------------------------------------
Assignment 02, Task 02
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports
from Food_utilities import average_calories, read_foods, _parse_bool, food_search
from Food import Food

# Constants


fh = open("foods.txt", "r")
foods = read_foods(fh)

origin = int(input("Enter an origin: "))
o_name = Food.ORIGIN[origin]

max_cals = int(input("Enter a max calories value: "))

is_veg = _parse_bool(input("Only display vegetarian foods? "))

search_results = food_search(foods, origin, max_cals, is_veg)
print(
    f"The average calories in the selected foods is {average_calories(search_results)}")
