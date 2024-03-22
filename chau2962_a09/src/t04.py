"""
-------------------------------------------------------
Assignment 09, Task 04
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-03-21"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

# Constants
SEP = '-' * 20


tree = BST()
for i in range(11):
    tree.insert(i)
print("Testing tree: ", list(tree))

print(SEP)

print("Test tree.node_counts():")
print(tree.node_counts())

print(SEP)

print("Testing tree.__contains__()")
print(f"7 in tree: {7 in tree}")
print(f"11 in tree: {11 in tree}")

print(SEP)

print("Testing tree.parent(7):")
print(tree.parent(7))

print(SEP)

print("Testing tree.parent_r(7):")
print(tree.parent_r(7))
