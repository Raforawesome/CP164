"""
-------------------------------------------------------
Lab 02, Task 02
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import array_to_stack

# Constants


inp: list[int] = [int(x.strip()) for x in input(
    "Enter a list of comma-seperated numbers: ").split(',')]

stack: Stack = Stack()
array_to_stack(stack, inp)

if not stack.is_empty():
    print(f"Created stack, peeking top: {stack.peek()}")
else:
    print("Created empty stack.")
