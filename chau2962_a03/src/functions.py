"""
-------------------------------------------------------
Assignment 3 Functions
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
import time
from Stack_array import Stack
import string as string_lib

# Constants


def input_stack() -> Stack:
    target: Stack = Stack()
    print("Enter digits for stack (enter non-number to end)")
    while True:
        try:
            target.push(int(input("Next number: ")))
        except ValueError:
            break
    return target


def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()
    while not source1.is_empty() or not source2.is_empty():
        if not source1.is_empty():
            target.push(source1.pop())
        if not source2.is_empty():
            target.push(source2.pop())
    return target


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    buffer = []
    while not source.is_empty():
        buffer.append(source.pop())
    for v in buffer:
        source.push(v)


# Not really constants?
PUNCTUATION = set(string_lib.punctuation)


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    chars = Stack()
    filtered = ""
    for c in string:
        if c.isnumeric() or c.isspace() or c in PUNCTUATION:
            continue
        else:
            filtered += c.lower()
    palindrome = True
    half = len(filtered) // 2
    ptr = 0

    while ptr < half:
        c = filtered[ptr]
        chars.push(c)
        ptr += 1
    if len(string) % 2 != 0:
        ptr += 1
    while ptr < len(filtered):
        c = filtered[ptr]
        ptr += 1
        if c != chars.pop():
            palindrome = False
            break
    return palindrome


# Constants
OPERATORS = "+-*/"


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    terms = string.strip().split(" ")
    stack = Stack()
    for c in terms:
        if c in OPERATORS:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if c == "+":
                stack.push(operand1 + operand2)
            elif c == "-":
                stack.push(operand1 - operand2)
            elif c == "*":
                stack.push(operand1 * operand2)
            elif c == "/":
                stack.push(operand1 / operand2)
        elif c.isnumeric():
            stack.push(int(c))
    answer = stack.pop()
    return answer


def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            does not include 'Start', but does include 'X'.
            Return None if there is no exit (list of str)
    -------------------------------------------------------
    """
    path = []
    path.append(maze["Start"][0])
    visited = set()
    while len(path) > 0 and path[-1] != "X":
        current = maze[path[-1]]  # get the possible paths
        visited.add(path[-1])  # mark node as visited
        cont = False  # no loop labels in python
        for v in current:
            if v == 'X':
                path.append(v)
                break  # end early if we find the exit
            elif v not in visited:
                path.append(v)  # Check next node
                cont = True
                break
        if not cont and path[-1] != "X":
            path.pop()  # if no X and no unvisited, back out

    if len(path) == 0 or path[-1] != "X":  # discard path if there is no exit
        path = None
    return path
