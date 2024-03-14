"""
-------------------------------------------------------
Assignment 07, Task 02
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-03-09"
-------------------------------------------------------
"""
# Imports
from Sorted_List_linked import Sorted_List
from copy import deepcopy
from Food import Food

# Constants


# Sample Food Data for Testing
food1 = Food("Apple", 0, True, 50)
food2 = Food("Pasta", 1, False, 200)
food3 = Food("Spinach", 2, True, 20)
food4 = Food("Beef", 3, False, 350)
food5 = Food("Apple", 0, True, 50)  # Duplicate of food1

foods = [food1, food2, food3, food4, food5]

empty_list = Sorted_List()
list1 = Sorted_List()
list2 = Sorted_List()
list3 = Sorted_List()

list1.insert(food1)
for i in range(0, 3):
    list2.insert(foods[i])
for f in foods:
    list3.insert(f)


# __contains__ tests
assert food1 in list1
assert food2 in list2
assert food5 in list3  # Checks if duplicates are handled correctly
assert food1 not in empty_list

# __eq__ tests
assert list2 != list3  # Assuming they're unequal due to duplicates

# __getitem__ tests
assert list2[0] == food1

# _linear_search tests (assuming method is exposed)
_, _, i = list3._linear_search(food3)
assert i - 1 == 2  # Index of food3

# clean tests
list3.clean()
assert list3 == deepcopy(list3)

# count tests
assert list2.count(food3) == 1

# find tests (Assuming 'find' returns the first matching item)
assert list3.find(food1) == food1
assert list3.find(Food("Apple", 0, True, 50)) == food1

# index tests
assert list2.index(food2) == 1

# insert tests
item = Food("Carrot", 2, True, 30)
list2.insert(item)
assert list2 == deepcopy(list2)

# max and min tests (Depend on how sorting is defined in the Sorted_List)
assert list3.max() == food4
assert list3.min() == food1

# peek tests
assert list3.peek() == food1  # Or food4 depending on sorting order

# remove tests
list3.remove(food1)
assert list3.count(food1) == 0  # If duplicates handled otherwise list1 not in list3

# remove_front tests
list3.remove_front()
assert list3[0] == food3  # Or next element based on sort order

print("All tests passed!")
