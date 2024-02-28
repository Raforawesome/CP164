"""
-------------------------------------------------------
Assignment 03, Task 04
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from functions import input_stack

# Constants


print("Input stack:")
stack = input_stack()
print()
print(f"Using stack {list(stack)}")
stack.reverse()
print(f"Reversed stack: {list(stack)}")
