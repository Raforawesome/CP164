"""
-------------------------------------------------------
Circular array version of the Queue ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-05-07"
-------------------------------------------------------
"""
# pylint: disable=protected-access

from copy import deepcopy


class Queue:
    """
    -------------------------------------------------------
    Constants
    -------------------------------------------------------
    """
    # a default maximum size when one is not provided
    DEFAULT_CAPACITY = 10

    def __init__(self, capacity=DEFAULT_CAPACITY):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a fixed-size list.
        Use: target = Queue(capacity)
        Use: target = Queue()  # uses default capacity
        -------------------------------------------------------
        Parameters:
            capacity - maximum size of the queue (int > 0)
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        assert capacity > 0, "Queue size must be > 0"

        self._capacity = capacity
        self._values = [None] * self._capacity
        self._front = None   # queue has no data
        self._rear = 0       # first available index for insertion
        self._count = 0      # number of data items

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: empty = source.is_empty()
        -------------------------------------------------------
        Returns:
            True if the queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: full = source.is_full()
        -------------------------------------------------------
        Returns:
            True if the queue is full, False otherwise.
        -------------------------------------------------------
        """
        return self._count >= self._capacity

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
            the number of values in the queue.
        -------------------------------------------------------
        """
        return self._count

    def __eq__(self, target):
        """
        ----------------
        Determines whether two Queues are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a queue (Queue)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        ---------------
        """
        equals = True
        if len(self) == len(target):
            i1 = self._front is not None and self._front or 0
            i2 = target._front is not None and target._front or 0
            stop = (i1 - self._count) % self._capacity
            if i1 == stop:
                equals = self._values[i1] == target._values[i2]
                i1 = (i1 + 1) % self._capacity
                i2 = (i2 + 1) % target._capacity
            while i1 != stop and equals is True:
                equals = self._values[i1] == target._values[i2]
                i1 = (i1 + 1) % self._capacity
                i2 = (i2 + 1) % target._capacity
        else:
            equals = False
        return equals

    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the rear of the queue.
        Use: source.insert( value )
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot add to a full queue"
        self._rear = (self._rear + 1) % self._capacity
        self._count += 1
        if self._front is not None and \
                self._rear - self._front == 1 and \
                self._count > 1:
            self._rear = None
        elif self._front is None:
            self.rear_forward()
            self._front = (self._rear - 1) % self._capacity
        self._values[self._rear - 1] = deepcopy(value)
        return None

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: v = source.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
                removed from the queue (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty queue"
        v = self.peek()
        self.front_forward()
        self._count -= 1
        if self._count == 0:
            self._front = None
        if self._rear is None:
            self._rear = (self._front - self._count - 2) % self._capacity
        return v

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: v = source.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of the queue -
                the value is not removed from the queue (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot peek at an empty queue"
        value = deepcopy(self._values[self._front])
        return value

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in cq:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        if self._front is not None:
            # queue is not empty
            j = self._front
            i = 0

            while i < self._count:
                yield self._values[j]
                i += 1
                j = (j + 1) % self._capacity

    def rear_back(self):
        self._rear = (self._rear - 1) % self._capacity

    def rear_forward(self):
        self._rear = (self._rear + 1) % self._capacity

    def front_back(self):
        self._front = (self._front - 1) % self._capacity

    def front_forward(self):
        self._front = (self._front + 1) % self._capacity

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source queue into separate target queues with values
        alternating into the targets. At finish source queue is empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Queue)
            target2 - contains remaining values from source (Queue)
        -------------------------------------------------------
        """
        target1 = Queue()
        target2 = Queue()
        debounce = False
        for v in self._values:
            if debounce is False:
                target1.insert(v)
            else:
                target2.insert(v)
            debounce = not debounce
        self._values.clear()  # faster than doing .remove(0) every time
        self._front = None
        self._rear = 0
        return target1, target2
