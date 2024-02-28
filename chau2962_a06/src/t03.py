"""
-------------------------------------------------------
Assignment 06, Task 03
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-02-18"
-------------------------------------------------------
"""
# Imports
from Deque_linked import Deque

# Constants


# Construction
d = Deque()
assert len(d) == 0
assert d.is_empty() is True
print("Construction test passed!")

# Insert and Remove (Front and Rear)
d.insert_front(1)
d.insert_rear(2)
d.insert_front(0)
assert len(d) == 3
assert d.is_empty() is False
assert d.remove_front() == 0
assert d.remove_rear() == 2
assert d.remove_front() == 1
assert d.is_empty() is True
print("Insert and remove (Front and Rear) test passed!")

# Peek
d.insert_front(10)
d.insert_rear(20)
assert d.peek_front() == 10
assert d.peek_rear() == 20
assert len(d) == 2
print("Peek test passed!")

# Equality
d1 = Deque()
d2 = Deque()
assert d1 == d2
d1.insert_front(1)
d1.insert_rear(2)
d2.insert_front(1)
d2.insert_rear(2)
assert d1 == d2
print("Equality test passed!")

# Swapping
d3 = Deque()
d3.insert_front(1)
d3.insert_rear(2)
d3.insert_rear(3)
d3.insert_rear(4)
d3._swap(d3._front, d3._rear)
assert d3.peek_front() == 4
assert d3.peek_rear() == 1
print("Swapping test passed!")

# Iteration
d4 = Deque()
for i in range(5):
    d4.insert_rear(i)
assert list(d4) == [0, 1, 2, 3, 4]
print("Iteration test passed!")
