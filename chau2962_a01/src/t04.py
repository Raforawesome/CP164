"""
-------------------------------------------------------
Assignment 01, Task 04
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-01-11"
-------------------------------------------------------
"""
# Imports
from functions import file_analyze

# Constants


file_name: str = input("Enter a file to analyze: ").strip()
file_handle = open(file_name, "r")
print(f"file_analyze(<File: {file_name}>) -> {file_analyze(file_handle)}")
