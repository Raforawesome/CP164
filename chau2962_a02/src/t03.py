"""
-------------------------------------------------------
Assignment 02, Task 03
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports
from Food_utilities import calories_by_origin, read_foods
from Food import Food

# Constants


fh = open("foods.txt", "r")
foods = read_foods(fh)
origin = int(input("Enter an origin: "))
o_name = Food.ORIGIN[origin]
print(
    f"The average calories in foods.txt \
with origin ID {origin} ({o_name}): {calories_by_origin(foods, origin)}"
)
