from functions import stack_maze

maze1 = {
    'Start': ['A', 'B'],
    'A': ['C', 'X'],
    'B': ['D'],
    'C': ['X'],
    'D': ['X'],
}

maze2 = {
    'Start': ['A', 'B'],
    'A': ['C'],
    'B': ['D', 'E'],
    'C': ['X'],
    'D': ['X'],
    'E': ['F', 'X'],
    'F': ['X'],
}

maze3 = {
    'Start': ['A', 'B', 'C'],
    'A': ['D', 'X'],
    'B': ['X'],
    'C': ['D', 'E'],
    'D': ['X'],
    'E': ['X'],
}

path1 = stack_maze(maze1)
print("Path to Exit:", path1)

path2 = stack_maze(maze2)
print("Path to Exit:", path2)

path3 = stack_maze(maze3)
print("Path to Exit:", path3)
