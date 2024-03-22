"""
-------------------------------------------------------
Tests various linked sorting functions.
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
from List_linked import List
from Number import Number
from Sorts_List_linked import Sorts

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
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted List of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """
    values = List()
    for i in range(0, SIZE):
        values.append(Number(i))
    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed List of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """
    values = List()
    for i in range(SIZE - 1, -1, -1):
        values.append(Number(i))
    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        lists - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of List of Number)
    -------------------------------------------------------
    """
    lists = List()
    for _ in range(TESTS):
        values = List()
        for _ in range(SIZE):
            values.append(Number(random.randint(0, XRANGE)))
        lists.append(values)
    return lists


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
    Tests a sort function with Number data and prints the number
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of Lists in random order.
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
    return
