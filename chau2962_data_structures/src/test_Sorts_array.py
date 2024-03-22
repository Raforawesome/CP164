"""
-------------------------------------------------------
Tests various array-based sorting functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2019-04-27"
-------------------------------------------------------
"""
# Imports
import math
import random
from re import L
from Number import Number
from Sorts_array import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted list of SIZE Number objects with values
	from 0 up to SIZE-1.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """
    values = [Number(i) for i in range(0, SIZE)]
    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of SIZE Number objects with values
	from SIZE-1 down to 0.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """
    values = [Number(i) for i in range(SIZE - 1, -1, -1)]
    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        arrays - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of list of Number)
    -------------------------------------------------------
    """
    arrays = [[Number(random.randint(0, XRANGE)) for _ in range(SIZE)] for _ in range(TESTS)]
    return arrays


# def get_comps(arr: list[Number]) -> int:
#     total: int = 0
#     for n in arr:
#         total += n.comparisons
#     return total
def comps() -> int:
    total: int = Number.comparisons
    Number.comparisons = 0
    return total


def swaps() -> int:
    total: int = Sorts.swaps
    Sorts.swaps = 0
    return total


def round(n: float) -> int:
    return math.floor(n + 0.5) == math.floor(n) and math.floor(n) or math.ceil(n)


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and prints the number
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of arrays in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """
    in_order, rev_order, rand_order = create_sorted(), create_reversed(), create_randoms()
    in_comps, rev_comps, rand_comps = 0, 0, 0
    in_swaps, rev_swaps, rand_swaps = 0, 0, 0
    Number.comparisons = 0
    Sorts.swaps = 0
    func(in_order)
    in_comps = comps()
    in_swaps = swaps()
    func(rev_order)
    rev_comps = comps()
    rev_swaps = swaps()

    for li in rand_order:
        func(li)
        rand_comps += comps()
        rand_swaps += swaps()
    rand_comps /= len(rand_order)
    rand_swaps /= len(rand_order)

    in_comps, rev_comps, rand_comps, in_swaps, rev_swaps, rand_swaps = \
    round(in_comps), round(rev_comps), round(rand_comps), \
    round(in_swaps), round(rev_swaps), round(rand_swaps)

    print(f"{title:<14} {in_comps:>8} {rev_comps:>8} {rand_comps:>8} {in_swaps:>8} {rev_swaps:>8} {rand_swaps:>8}")
    return None
