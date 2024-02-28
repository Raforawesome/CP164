"""
-------------------------------------------------------
Assignment 05, Task 01
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-02-10"
-------------------------------------------------------
"""
# Imports
from List_array import List

# Constants


def l2l(inp: list) -> List:
    new = List()
    new._values = inp
    return new


###########
# TESTING #
###########

# __eq__ testing
cases = [
    ([1, 2, 3], [1, 2, 3], True),
    ([1, 2, 3], [3, 2, 1], False),
    ([1, 2, 3], [1, 2], False),
    ([], [], True),
]

for inp1, inp2, cond in cases:
    print("Testing __eq__ with inputs:")
    print(inp1)
    print(inp2)
    assert (l2l(inp1) == l2l(inp2)) is cond, "Case failed!"
    print("Case passed")
    print()

print()


# __getitem__ testing
cases = [
    ([1, 2, 3], 1, 2),
    ([5, 6, 4, 3], 3, 3),
    ([6], 0, 6),
    ([7, 6, 5, 4], 1, 6),
]

for li, idx, val in cases:
    print("Testing __getitem__ with inputs:")
    print(li)
    print(idx)
    assert l2l(li)[idx] == val, "Case failed!"
    print("Case passed")
    print()

print()


# append testing
cases = [
    ([1, 2], 3, [1, 2, 3]),
    ([], 0, [0]),
]

for li, ins, res in cases:
    print("Testing append with inputs:")
    print(li, " + ", ins)
    print(res)
    l = l2l(li)
    l.append(ins)
    assert l == l2l(res), "Case failed!"
    print("Case passed")
    print()

print()


# clean testing
cases = [
    [[], []],
    [[1, 2, 3, 3], [1, 2, 3]],
    [[2, 2, 1, 3], [2, 1, 3]],
    [[1, 1, 1, 1, 1, 2, 3], [1, 2, 3]],
]

for inp, res in cases:
    print("Testing clean with inputs:")
    print(inp)
    print(res)
    li = l2l(inp)
    li.clean()
    assert li == l2l(res), "Case failed!"
    print("Case passed")
    print()

print()


# combine testing
cases = [
    [[1, 3], [2, 4], [1, 2, 3, 4]],
    [[1, 3, 5], [2, 4], [1, 2, 3, 4, 5]],
    [[], [2], [2]],
]

for in1, in2, res in cases:
    print("Testing combine with inputs:")
    print(inp)
    print(res)
    li = List()
    li.combine(l2l(in1), l2l(in2))
    assert li == l2l(res), "Case failed!"
    print("Case passed")
    print()

print()
