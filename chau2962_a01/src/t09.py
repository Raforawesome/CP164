"""
-------------------------------------------------------
Assignment 01, Task 09
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-01-11"
-------------------------------------------------------
"""
# Imports
from functions import matrixes_add
import random

# Constants
NUM_MIN = 0
NUM_MAX = 99


n = int(input("Enter a value 'n' to generate two n by n arrays: "))


matrix1 = []
print("Matrix 1:")

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
    matrix1.append(li)
    m_buf += '|'

m_buf += '\n'
m_buf += header
print(m_buf)


print()


matrix2 = []
print("Matrix 2:")

m_buf = ""
m_buf += header

for _ in range(n):
    li = []
    m_buf += '\n| '
    for _ in range(n):
        nn = random.randint(NUM_MIN, NUM_MAX)
        li.append(nn)
        m_buf += f"{nn:0>2d} "
    matrix2.append(li)
    m_buf += '|'

m_buf += '\n'
m_buf += header
print(m_buf)


print()


matrix3 = matrixes_add(matrix1, matrix2)
print("Sum of matrices:")

m_buf = ""
header = "-" * (4 * (n + 1))
m_buf += header

for row in range(n):
    li = []
    m_buf += '\n| '
    for column in range(n):
        nn = matrix3[row][column]
        li.append(nn)
        m_buf += f"{nn:0>3d} "
    matrix3.append(li)
    m_buf += '|'

m_buf += '\n'
m_buf += header
print(m_buf)
