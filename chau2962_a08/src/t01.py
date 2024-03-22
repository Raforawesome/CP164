"""
-------------------------------------------------------
Assignment 08, Task 01
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-03-16"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy
from BST_linked import BST

# Constants


# You'll need your complete BST class definition here. I'll assume you have it.

# Create a sample BST
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(8)
bst.insert(1)
bst.insert(4)

# Tests
print("Testing is_valid...")
assert bst.is_valid()  # Should be True

bst_alt = deepcopy(bst)
bst_alt._root._left._value = 6  # Breaks BST property
assert not bst_alt.is_valid()  # Should be False
print("is_valid Tests Passed")

print("Testing min...")
assert bst.min() == 1
print("min Test Passed")

print("Testing leaf_count...")
assert bst.leaf_count() == 3
print("leaf_count Test Passed")

print("Testing one_child_count...")
assert bst.one_child_count() == 0
print("one_child_count Test Passed")

print("Testing two_child_count...")
assert bst.two_child_count() == 2
print("two_child_count Test Passed")

print("Testing inorder...")
print(bst.inorder())
assert bst.inorder() == [1, 3, 4, 5, 8]
print("inorder Test Passed")

print("Testing preorder...")
print(bst.preorder())
assert bst.preorder() == [5, 3, 1, 4, 8]
print("preorder Test Passed")

print("Testing postorder...")
assert bst.postorder() == [1, 4, 3, 8, 5]
print("postorder Test Passed")

print("Testing levelorder...")
assert bst.levelorder() == [5, 3, 8, 1, 4]
print("levelorder Test Passed")

print("Testing remove...")
value = bst.remove(3)
assert value == 3
print("remove Test Passed")

print("Testing remove (non-existent)...")
assert bst.remove(10) is None  # Attempt to remove a non-existent key
print("remove (non-existent) Test Passed")
