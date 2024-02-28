"""
-------------------------------------------------------
Assignment 01, Task 08
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-01-11"
-------------------------------------------------------
"""
# Imports
from functions import matrix_stats
import random

# Constants
NUM_MIN = 1
NUM_MAX = 99


n = int(input("Enter a value 'n' to generate an n by n array: "))
matrix = []


print("Matrix:")

m_buf = ""
header = "-" * (3 * (n + 1))
m_buf += header

for _ in range(n):
    li = []
    m_buf += '\n| '
    for _ in range(n):
        nn = random.randint(NUM_MIN, NUM_MAX)
        li.append(nn)
        m_buf += f"{nn:0>2d} "
    matrix.append(li)
    m_buf += '|'

m_buf += '\n'
m_buf += header
print(m_buf)
print()
print(f"matrix_stats(<Matrix>) -> {matrix_stats(matrix)}")
