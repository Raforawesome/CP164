"""
-------------------------------------------------------
Assignment 08, Task 02
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
from functions import do_comparisons, comparison_total

# Constants
DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"


BST1 = BST()
BST2 = BST()
BST3 = BST()

BSTs = [BST1, BST2, BST3]
DATAs = [DATA1, DATA2, DATA3]
for i in range(0, 3):
    for c in DATAs[i]:
        BSTs[i].insert(Letter(c))


# Need new handle for each as iteration consumes
do_comparisons(open("miserables.txt", 'r'), BST1)
do_comparisons(open("miserables.txt", 'r'), BST2)
do_comparisons(open("miserables.txt", 'r'), BST3)

total1 = comparison_total(BST1)
total2 = comparison_total(BST2)
total3 = comparison_total(BST3)

sep = '-' * 60

print(f"Comparing by order: {DATA1}")
print(f"Total comparisons: {total1:,}")
print(sep)
print(f"Comparing by order: {DATA2}")
print(f"Total comparisons: {total2:,}")
print(sep)
print(f"Comparing by order: {DATA3}")
print(f"Total comparisons: {total3:,}")
