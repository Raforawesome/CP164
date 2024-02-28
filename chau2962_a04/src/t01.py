"""
-------------------------------------------------------
Assignment 04, Task 01
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-02-01"
-------------------------------------------------------
"""
# Imports
from Queue_circular import Queue

# Constants


def print_queue(q: Queue):
    print("Queue:")
    print(f"    values: {q._values}")
    print(f"    front: {q._front}")
    print(f"    rear: {q._rear}")
    print(f"    capacity: {q._capacity}")

##################
# Testing __eq__ #
##################


# Exact same queue
q1 = Queue()
q2 = Queue()
for i in range(1, 6):
    q1.insert(i)
    q2.insert(i)
assert q1 == q2, "Equality check 1 FAILED"
print("Equality check 1 PASSED")

# Same queue, different offsets
q1 = Queue()
q2 = Queue()
for _ in range(3):
    q2.insert(0)
    q2.remove()
for i in range(1, 6):
    q1.insert(i)
    q2.insert(i)
assert q1 == q2, "Equality check 2 FAILED"
print("Equality check 2 PASSED")

# Same queue, max len (test None checks)
q1 = Queue()
q2 = Queue()
for i in range(1, 11):
    q1.insert(i)
    q2.insert(i)
assert q1 == q2, "Equality check 3 FAILED"
print("Equality check 3 PASSED")

# Different queues, max len
q1 = Queue()
q2 = Queue()
for i in range(1, 11):
    q1.insert(i)
for i in range(2, 12):
    q2.insert(i)
assert q1 != q2, "Equality check 4 FAILED"
print("Equality check 4 PASSED")

# Empty queues
q1 = Queue()
q2 = Queue()
assert q1 == q2, "Equality check 5 FAILED"
print("Equality check 5 PASSED")

# one non-empty queue
q1 = Queue()
q1.insert(1)
q2 = Queue()
assert q1 != q2, "Equality check 6 FAILED"
print("Equality check 6 PASSED")

# one non-empty queue (reversed)
q1 = Queue()
q2 = Queue()
q2.insert(1)
assert q1 != q2, "Equality check 7 FAILED"
print("Equality check 7 PASSED")

# max queues different offsets
q1 = Queue()
q2 = Queue()
q2.insert(0)
q2.remove()
for i in range(1, 11):
    q1.insert(i)
    q2.insert(i)
print_queue(q1)
print_queue(q2)
assert q1 == q2, "Equality check 8 FAILED"
print("Equality check 8 PASSED")
