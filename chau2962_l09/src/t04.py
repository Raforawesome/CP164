"""
-------------------------------------------------------
Lab 09, Task 04
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-03-14"
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set

# Constants


source: Hash_Set = Hash_Set(5)
for n in [55, 11, 22, 33, 44]:
    source.insert(n)
source.debug()
source._rehash()
source.debug()
