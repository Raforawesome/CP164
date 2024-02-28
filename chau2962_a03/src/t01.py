"""
-------------------------------------------------------
Assignment 03, Task 01
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from functions import input_stack, stack_combine

# Constants


print("Enter stack 1:")
stack1 = input_stack()
print()
print("Enter stack 2:")
stack2 = input_stack()

output = stack_combine(stack1, stack2)
print()
print("Combined stack:")
print(list(output))
