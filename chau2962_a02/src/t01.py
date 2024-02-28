"""
-------------------------------------------------------
Assignment 02, Task 01
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports
from Food_utilities import by_origin, read_foods
from Food import Food

# Constants


fh = open("foods.txt", "r")
foods = read_foods(fh)
origin = int(input("Enter an origin: "))
o_name = Food.ORIGIN[origin]
o_foods = by_origin(foods, origin)
print(f"Filtering foods.txt by origin ID {origin} ({o_name}):")
print(list(map(lambda f: f.name, o_foods)))
