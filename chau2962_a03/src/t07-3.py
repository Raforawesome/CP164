from functions import stack_maze

maze = {'Start': ['A'], 'A': ['B', 'X'], 'B': []}

path = stack_maze(maze)
print(path)
