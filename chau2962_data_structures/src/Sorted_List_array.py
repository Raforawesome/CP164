"""
-------------------------------------------------------
Array version of the Sorted_List ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-05-07"
-------------------------------------------------------
"""
from copy import deepcopy


class Sorted_List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_List.
        Use: target = Sorted_List()
        -------------------------------------------------------
        Returns:
            a Sorted_List object (Sorted_List)
        -------------------------------------------------------
        """
        self._values = []

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if source contains key.
        Use: b = key in source
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if source contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """
        contains = False
        ptr = 0
        while contains is False and ptr < len(self._values):
            if self._values[ptr] == key:
                contains = True
            ptr += 1
        return contains

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of source.
        Use: value = source[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of source (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'Invalid index value'
        value = deepcopy(self._values[i])
        return value

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of a sorted list.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
            the number of values in source.
        -------------------------------------------------------
        """
        return len(self._values)

    def _binary_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list.
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._binary_search(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - the index of the first occurrence of key in
                the list, -1 if key is not found. (int)
        -------------------------------------------------------
        """
        # Your code here

        return

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(Sorted_List) to len(Sorted_List) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        # Your code here

        return

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from source.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            source contains one and only one of each value formerly present
            in source. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        new = []
        last = None
        for (i, v) in enumerate(self._values):
            # list is sorted so equal values are adjacent
            if last is None or v != last:
                new.append(v)
            last = v
        self._values = new
        return None

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list.
        When finished, the contents of source1 and source2 are interlaced
        into target and source1 and source2 are empty.
        Values are sorted.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        # Your code here

        return

    def copy(self):
        """
        ---------------------------------------------------------
        Copies the contents of this list to another sorted list.
        Use: target = source.copy()
        -------------------------------------------------------
        Returns:
            target - a sorted list containing a copy of the contents
                of source (Sorted_List)
        -------------------------------------------------------
        """
        # Your code here

        return

    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in source.
        Use: n = source.count(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            number - the number of times key appears in source (int)
        -------------------------------------------------------
        """
        number = 0
        for v in self._values:
            if v == key:
                number += 1
        return number

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in source that matches key.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        value = None
        ptr = 0
        while value is None and ptr < len(self._values):
            if self._values[ptr] == key:
                value = deepcopy(self._values[ptr])
            ptr += 1
        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds the location of the first occurrence of key in source.
        Use: n = source.index(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - the location of the value matching key, otherwise -1 (int)
        -------------------------------------------------------
        """
        idx = None
        ptr = 0
        while idx is None and ptr < len(self._values):
            if self._values[ptr] == key:
                idx = ptr
            ptr += 1
        return idx is not None and idx or -1

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in source.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: source.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        low = 0
        high = len(self._values) - 1

        while low <= high:
            mid = (high - low) // 2 + low

            if self._values[mid] > value:
                high = mid - 1
            else:
                low = mid + 1

        self._values.insert(low, value)

        return None

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        l1 = len(source1._values)
        l2 = len(source2._values)
        max = l2 > l1 and l2 or l1
        for ptr in range(0, max):
            v1 = source1._values[ptr]
            v2 = source2._values[ptr]
            if v1 == v2:
                self._values.push(v1)
        return None

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if source is empty.
        Use: b = source.is_empty()
        -------------------------------------------------------
        Returns:
            True if source is empty, False otherwise.
        -------------------------------------------------------
        """
        # Your code here

        return

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Sorted_Lists are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a list (Sorted_Lists)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        equals = True
        if len(self._values) == len(target._values):
            i = 0
            lim = len(self)
            while i < lim and equals is True:
                if self[i] != target[i]:
                    equals = False
                i += 1
        else:
            equals = True
        return equals

    def max(self):
        """
        -------------------------------------------------------
        Returns the maximum value in source.
        Use: value = source.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in source (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot find maximum of an empty list'
        value = deepcopy(self._values[-1])  # values are sorted
        return value

    def min(self):
        """
        -------------------------------------------------------
        Returns the minimum value in source.
        Use: value = source.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in source (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot find minimum of an empty list'
        value = deepcopy(self._values[0])  # values are sorted
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in source.
        Use: value = source.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in source (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot peek at an empty list'
        value = deepcopy(self._values[0])
        return value

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in source with index i.
        Use: value = source.pop()
        Use: value = source.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
                args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], otherwise
                the last value in source, value is removed from source (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        if len(args) == 1:
            # pop the element at position i
            i = args[0]
            value = self._values.pop(i)
        else:
            # pop the last element
            value = self._values.pop()
        return value

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in source
        that matches key.
        Use: value = source.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        value = None
        i = 0
        while value is None and i < len(self._values):
            if self._values[i] == key:
                value = self._values.pop(i)
        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first item in source.
        Use: value = source.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot remove from an empty list'
        value = self._values.pop(0)
        return value

    def remove_many(self, key):
        """
        ---------------------------------------------------------
        Removes all values that match key in source.
        Use: source.remove_many(key)
        ---------------------------------------------------------
        Parameters:
            key - the key to match (?)
        Returns:
            None
        ---------------------------------------------------------
        """
        while key in self._values:
            self._values.remove(key)
        return None

    def split(self):
        """
        ---------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. source becomes empty.
        Use:  target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (Sorted_List)
            target2 - a new List with <= 50% of the original List (Sorted_List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        lenn = len(self._values)
        mid = lenn // 2
        ptr = 0
        while ptr < mid:
            target1.push(self._values[ptr])
            ptr += 1
        if lenn % 2 != 0:
            target1.push(self._values[ptr])
            ptr += 1
        while ptr < lenn:
            target2.push(self._values[ptr])
            ptr += 1
        self._values.clear()  # faster than always popping at 0
        return target1, target2

    def split_alt(self):
        """
        -------------------------------------------------------
        Split a List into two parts. target1 contains the even indexed
        elements, target2 contains the odd indexed elements.
        source is empty after the function executes.
        (iterative version)
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - the even indexed elements of the list (Sorted_List)
            target2 - the odd indexed elements of the list (Sorted_List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        db = False
        ptr = 0
        while ptr < len(self._values):
            val = self._values[ptr]
            if db is False:
                target1._values.append(val)
            else:
                target2._values.append(val)
            ptr += 1
            db = not db
        self._values.clear()  # faster than always popping at 0
        return target1, target2
        return

    def split_apply(self, func):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains all the values
        where the result of calling func(value) is True, target2 contains
        the remaining values. At finish, self is empty. Order of values
        in targets is maintained.
        Use: target1, target2 = source.split_apply(func)
        -------------------------------------------------------
        Parameters:
            func - a function that given a value in the list returns
                True for some condition, otherwise returns False.
        Returns:
            target1 - a new List with values where func(value) is True (List)
            target2 - a new List with values where func(value) is False (List)
        -------------------------------------------------------
        """
        # Your code here

        return

    def split_key(self, key):
        """
        ---------------------------------------------------------
        Splits list into two parts. target1 contains all values < key,
        target2 all values >= key. source becomes empty. source is
        empty at end.
        Use:  target1, target2 = source.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            target1 - a new Sorted List with values < key (Sorted_List)
            target2 - a new Sorted List with values >= key (Sorted_List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        lenn = len(self._values)
        mid = lenn // 2
        found = False
        i = 0
        while i < len(self._values) and found is False:
            if self._values[i] == key:
                found = True
            target1._values.append(self._values[i])
            i += 1
        return

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        ptr1 = 0
        ptr2 = 0
        max1 = len(source1._values)
        max2 = len(source2._values)
        while ptr1 < max1 or ptr2 < max2:
            if ptr1 < max1 and ptr2 < max2:
                v1 = source1._values[ptr1]
                v2 = source2._values[ptr2]
                if v2 < v1 and v2 not in self._values:
                    self._values.append(v2)
                    ptr2 += 1
                elif v1 not in self._values:
                    self._values.append(v1)
                    ptr1 += 1
            elif ptr1 < max1:
                v = source1._values[ptr1]
                if v not in self._values:
                    self._values.push(v)
                ptr1 += 1
            else:
                v = source2._values[ptr2]
                if v not in self._values:
                    self._values.push(v)
                ptr2 += 1
        return None

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through source
        from front to rear.
        Use: for value in source:
        -------------------------------------------------------
        Returns:
            value - the next value in source (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
