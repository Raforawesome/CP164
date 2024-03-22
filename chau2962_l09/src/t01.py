"""
-------------------------------------------------------
Lab 09, Task 01
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-03-14"
-------------------------------------------------------
"""
# Imports
from functions import hash_table
from Food import Food

# Constants


# Food(name, origin, is_veg, cals)
foods = [
    Food("Butter Chicken", 2, False, 250),
    Food("Lasagna", 7, False, 250),
    Food("Moo Goo Gai Pan", 1, False, 250),
    Food("Vegetable Alicha", 3, True, 250),
]

hash_table(11, foods)
