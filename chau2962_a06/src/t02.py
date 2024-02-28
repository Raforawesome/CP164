"""
-------------------------------------------------------
Assignment 06, Task 02
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-02-18"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_linked import Priority_Queue

# Constants


# Test Cases

# Construction
pq = Priority_Queue()
assert len(pq) == 0
assert pq.is_empty() is True
print("Construction test passed!")

# Insert and Remove (Priority Order)
pq.insert(5)
pq.insert(3)
pq.insert(8)
assert len(pq) == 3
assert pq.is_empty() is False
assert pq.remove() == 3
assert pq.remove() == 5
assert pq.remove() == 8
assert pq.is_empty() is True
print("Insert and remove test passed!")

# Peek
pq.insert(10)
assert pq.peek() == 10
assert len(pq) == 1
print("Peek test passed!")

# Combine (Interlacing)
pq1 = Priority_Queue()
pq1.insert(3)
pq1.insert(1)
pq2 = Priority_Queue()
pq2.insert(4)
pq2.insert(2)
pq3 = Priority_Queue()
pq3.combine(pq1, pq2)
assert list(pq3) == [1, 2, 3, 4]
assert len(pq3) == 4
assert pq2.is_empty() is True
assert pq1.is_empty() is True
print("Combine (interlacing) test passed!")

# Split Alternate
pq = Priority_Queue()
for i in range(6):
    pq.insert(i)
q1, q2 = pq.split_alt()
assert list(q1) == [0, 2, 4]
assert list(q2) == [1, 3, 5]
print("Split alternate test passed!")
