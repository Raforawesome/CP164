
"""
-------------------------------------------------------
Assignment 08 Functions
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-03-16"
-------------------------------------------------------
"""
# Imports
from Letter import Letter
from BST_linked import BST


def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    # Zeroes out all comparison values in tree nodes
    for node in bst:
        node.comparisons = 0

    for line in file_variable:
        for char in line:
            if char.isalpha():
                char: str = char.upper()
                cobj: Letter = Letter(char)
                found: Letter = bst.retrieve(cobj)
                assert found == cobj, "BST retrieve function is wrong!"
    return None


def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    total = 0
    letters = bst.inorder()

    for obj in letters:
        total += obj.comparisons

    return total


def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    letters = bst.inorder()
    total = 0
    for l in letters:
        total += l.comparisons
    s_count =  10 + 7 + 6 + 2
    sep = '-' * s_count

    print("Letter Count/Percent Table")
    print()
    print(f"Total Count: {total:,}")
    print()
    print(f"{'LETTER'} {'COUNT':>10} {'%':>7}")
    print(sep)
    for l in letters:
        print(f"{l.letter:>6} {f'{l.comparisons:,}':>10} {f'{l.comparisons/total:06.2%}':>7}")

    return None
