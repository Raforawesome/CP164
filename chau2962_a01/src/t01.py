"""
-------------------------------------------------------
Assignment 01, Task 01
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-01-11"
-------------------------------------------------------
"""
# Imports
from functions import clean_list

# Constants


inp: list[int] = [int(x.strip()) for x in input(
    "Enter a list of comma-seperated numbers: ").split(',')]
print(f"clean_list({inp}) ->:")
clean_list(inp)
print(inp)
