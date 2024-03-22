"""
-------------------------------------------------------
Lab 10, Task 03
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-03-24"
-------------------------------------------------------
"""
# Imports
from test_Sorts_array import test_sort, SORTS, SIZE


# Constants
L1 = '-' * 14
L2 = '-' * 8


print(f"n: {SIZE:<11} |{'Comparisons':^24}| |{'Swaps':^24}|")
print(f"{'Algorithm':<14} {'In Order':>8} {'Reversed':>8} {'Random':>8} {'In Order':>8} {'Reversed':>8} {'Random':>8}")
print(f"{L1} {L2} {L2} {L2} {L2} {L2} {L2}")
for (name, func) in SORTS:
    test_sort(name, func)
