"""
-------------------------------------------------------
Assignment 04, Task 02
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-02-01"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from functions import queue_split_alt

# Constants


q1 = Queue()
q2 = Queue()
q3 = Queue()

for i in range(1, 11):
    q1.insert(i)
for i in range(10, 0, -1):
    q2.insert(i)

t1, t2 = queue_split_alt(q1)
t3, t4 = queue_split_alt(q2)
t5, t6 = queue_split_alt(q3)

assert q1.is_empty(), "Queue 1 is not empty"
assert q2.is_empty(), "Queue 2 is not empty"
assert q3.is_empty(), "Queue 3 is not empty"
print("All queues are empty.")
print()
print(f"split queues from {list(q1)}: {list(t1)}, {list(t2)}")
print(f"split queues from {list(q2)}: {list(t3)}, {list(t4)}")
print(f"split queues from {list(q3)}: {list(t5)}, {list(t6)}")
