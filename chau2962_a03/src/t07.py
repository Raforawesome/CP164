"""
-------------------------------------------------------
Assignment 03, Task 07
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from functions import stack_maze

# Constants


maze1 = {'Start': ['A'], 'A': ['B', 'C'], 'B': [], 'C': ['D', 'E'],
         'D': [], 'E': ['F', 'X'], 'F': ['G', 'H'], 'G': [], 'H': []}
maze2 = {'Start': ['X']}
maze3 = {'Start': ['A'], 'A': ['B', 'C'], 'B': [], 'C': ['D', 'E'],
         'D': [], 'E': ['X', 'F'], 'F': ['G'], 'G': ['C']}
maze4 = {'Start': ['A'], 'A': []}

mazes = [maze1, maze2, maze3, maze4]

for (i, maze) in enumerate(mazes):
    print(f"Maze Test #{i}")
    print("Maze:")
    print(maze)
    print()
    print("Solution:")
    print(stack_maze(maze))
    print()
    print()
    print()
