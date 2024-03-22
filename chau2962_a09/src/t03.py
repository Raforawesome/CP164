"""
-------------------------------------------------------
Assignment 09, Task 03
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-03-21"
-------------------------------------------------------
"""
# Imports
from functions import insert_words, comparison_total
from Hash_Set_BST import Hash_Set

# Constants


fv = open('otoos610.txt', 'r')
hash_set = Hash_Set(20)

insert_words(fv, hash_set)
total, max_word = comparison_total(hash_set)

print("Using linked BST Hash_Set")
print()
print(f"Total Comparisons: {total:,}")
print(f"Word with maximum comparisons '{max_word.word}': {max_word.comparisons:,}")
