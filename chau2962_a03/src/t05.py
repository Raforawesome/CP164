"""
-------------------------------------------------------
Assignment 03, Task 05
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# imports
from functions import is_palindrome_stack

# constants


string = input("enter a string to check: ")
is_palin = is_palindrome_stack(string)

print(f"is_palindrome_stack(\"{string}\") -> {str(is_palin)}")
