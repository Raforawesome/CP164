"""
-------------------------------------------------------
Assignment 01, Task 02
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-01-11"
-------------------------------------------------------
"""
# Imports
from functions import list_subtraction

# Constants


minuend: list[int] = [int(x.strip()) for x in input(
    "Enter a list of comma-seperated numbers: ").split(',')]
subtrahend: list[int] = [int(x.strip()) for x in input(
    "Enter a list of comma-seperated numbers to remove: ").split(',')]
print(f"list_subtraction({minuend}, {subtrahend}) ->:")
list_subtraction(minuend, subtrahend)
print(f"{minuend}")
