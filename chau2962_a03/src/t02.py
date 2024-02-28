"""
-------------------------------------------------------
Assignment 03, Task 02
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


print("Enter initial stack:")
initial_stack = input_stack()
print()
print("Enter source 1:")
stack1 = input_stack()
print()
print("Enter source 2:")
stack2 = input_stack()

print()
initial_stack.combine(stack1, stack2)

print("Combined stacks:")
print(list(initial_stack))
