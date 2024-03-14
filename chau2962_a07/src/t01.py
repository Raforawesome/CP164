"""
-------------------------------------------------------
Assignment 07, Task 01
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-03-09"
-------------------------------------------------------
"""
# Imports
from List_linked import List
from Food import Food
from copy import deepcopy


# Constants


# Sample Food Data for Testing
food1 = Food("Apple", 0, True, 50)
food2 = Food("Pasta", 1, False, 200)
food3 = Food("Spinach", 2, True, 20)
food4 = Food("Beef", 3, False, 350)
food5 = Food("Apple", 0, True, 50)  # Duplicate of food1

foods = [food1, food2, food3, food4, food5]

empty_list = List()
list1 = List()
list2 = List()
list3 = List()

list1.append(food1)
for i in range(0, 3):
    list2.append(foods[i])
for f in foods:
    list3.append(f)

# ------------------
# Test __eq__
# ------------------
#
print("Empty list == Empty list:")
print(empty_list == List())

print("list3 == list3:")
print(list3 == list3)

print("list2 == list3:")
print(list2 == list3)

# ------------------
# Test __getitem__
# ------------------
item = list3[2]
assert item == foods[2]        # Check item retrieval at index 2

# Boundary Test
try:
   item = list3[10]
except AssertionError:
   assert True

# ------------------
# Test append (assuming this now exists)
# ------------------
list3.append(food4)
assert len(list3) == len(foods) + 1
assert list3[-1] == food4

# --------------
# Test clean
# --------------
list3.append(food5)  # Duplicate
initial_length = len(list3)
list3.clean()
print(len(list3), initial_length - 1)

# ----------------
# Test combine
# ---------------
list5 = List()
list5.combine(deepcopy(list3), deepcopy(list2))

# -------------------
# Test intersection
# -------------------
list6 = List()
list6.append(food3)
list6.append(food4)

result_list = list3.intersection(list6, deepcopy(list5))

# ------------------
# Test prepend
# ------------------
list3.prepend(food4)

# -----------------
# Test remove_front
# ------------------
list3.remove_front()

# -----------------
# Test remove_many
# -----------------
list3.remove_many(food1)

# -----------
# Test split
# -----------
list_a, list_b = list3.split()

# -----------
# Test split_alt
# -----------
list_a, list_b = list3.split_alt()

# -----------
# Test union
# -----------
result_list = list3.union(list6, deepcopy(list5))

print("All tests passed!")
