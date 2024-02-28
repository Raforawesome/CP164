"""
-------------------------------------------------------
Assignment 4 Functions
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue

# Constants


def queue_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source queue into separate target queues with values
    alternating into the targets. At finish source queue is empty.
    Order of source values is preserved.
    (iterative algorithm)
    Use: target1, target2 = queue_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - a queue (Queue)
    Returns:
        target1 - contains alternating values from source (Queue)
        target2 - contains other alternating values from source (Queue)
    -------------------------------------------------------
    """
    debounce = False
    target1 = Queue()
    target2 = Queue()
    li = []
    while not source.is_empty():
        li.append(source.remove())
    li.reverse()
    for v in li:
        if debounce is False:
            target1.insert(v)
        else:
            target2.insert(v)
        debounce = not debounce
    return target1, target2


def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    li = []
    while not source.is_empty():
        li.append(source.remove())
    li.reverse()
    for v in li:
        if v > key:
            target1.insert(v)
        else:
            target2.insert(v)
    return target1, target2
