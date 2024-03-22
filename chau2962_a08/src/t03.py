"""
-------------------------------------------------------
Assignment 08, Task 03
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-03-16"
-------------------------------------------------------
"""
# Imports
from Letter import Letter
from BST_linked import BST
from functions import do_comparisons, letter_table

# Constants
DATA = "ETAOINSHRDLUCMPFYWGBVKJXZQ"


bst = BST()
for l in DATA:
    bst.insert(Letter(l))

do_comparisons(open("miserables.txt", 'r'), bst)
letter_table(bst)
