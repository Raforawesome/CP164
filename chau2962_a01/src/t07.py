"""
-------------------------------------------------------
Assignment 01, Task 07
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-01-11"
-------------------------------------------------------
"""
# Imports
from functions import max_diff

# Constants


lis: list[int] = [int(x.strip()) for x in input(
    "Enter a list of comma-seperated numbers: ").split(',')]
print(f"max_diff({lis}) -> {max_diff(lis)}")
