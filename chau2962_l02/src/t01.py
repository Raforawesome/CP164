"""
-------------------------------------------------------
Lab 02, Task 01
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack

# Constants


inp: list[int] = [int(x.strip()) for x in input(
    "Enter a list of comma-seperated numbers: ").split(',')]


def yesify(inp: bool) -> str:
    if inp is True:
        return "Yes"
    else:
        return "No"


stack: Stack = Stack()
print(f"Is stack empty: {yesify(stack.is_empty())}")

for v in inp:
    print(f"Pushing {v} onto stack...")

print(f"Is stack empty: {yesify(stack.is_empty())}")

print(f"Peeking top of stack: {stack.peek()}")

i: int = 0
while not stack.is_empty():
    print(f"Pop #{i}: {stack.pop()}")
    i += 1

print(f"Is stack empty: {yesify(stack.is_empty())}")
