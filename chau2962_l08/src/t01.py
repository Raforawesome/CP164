"""
-------------------------------------------------------
Lab 06, Task 01
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-02-17"
-------------------------------------------------------
"""
# Imports
from List_linked import List

# Constants


li = List()
li2 = [1, 2, 3, 4, 5]
for v in li2:
    li.insert(100, v)
print(li2)
print(list(li))
