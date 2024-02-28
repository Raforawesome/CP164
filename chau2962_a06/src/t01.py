"""
-------------------------------------------------------
Assignment 06, Task 01
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-02-18"
-------------------------------------------------------
"""
# Imports
from Queue_linked import Queue

# Constants


# Construction
q = Queue()
assert list(q) == []
print("Construction test passed!")

# Insert and Remove (FIFO)
q.insert("hello")
q.insert("world")
assert list(q) == ["hello", "world"]
assert q.remove() == "hello"
assert q.remove() == "world"
assert list(q) == []
print("Insert and remove test passed!")

# Peek
q.insert(10)
assert q.peek() == 10
assert list(q) == [10]
print("Peek test passed!")

# Combine (Interlacing)
q1 = Queue()
q1.insert('A')
q1.insert('B')
q2 = Queue()
q2.insert('C')
q2.insert('D')
q3 = Queue()  # Create a new blank queue
q3.combine(q1, q2)  # Combine q1 and q2 into q3
assert list(q3) == ['A', 'C', 'B', 'D']
print("Combine (interlacing) test passed!")

# ... (Rest of the code)

# Split Alternate
q = Queue()
for i in range(6):
    q.insert(i)
q1, q2 = q.split_alt()
assert list(q1) == [0, 2, 4]
assert list(q2) == [1, 3, 5]
print("Split alternate test passed!")
