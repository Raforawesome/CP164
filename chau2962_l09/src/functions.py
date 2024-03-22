"""
-------------------------------------------------------
Lab 09 Functions
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-03-14"
-------------------------------------------------------
"""
# Imports

# Constants
SEP = '-' * 8 + ' ' + '-' * 4 + ' ' + '-' * 20


def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
    Hash     Slot Key
    -------- ---- --------------------
         695    2 Lasagna, 7
        1355    4 Butter Chicken, 2
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    print(f"{'Hash':<8} {'Slot':>4} {'Key':<20}")
    print(SEP)
    for value in values:
        key = value.key()
        hsh = hash(value)
        slot = hsh % slots
        print(f"{hsh:>8} {slot:>4} {key:<20}")
    return None
