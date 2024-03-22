"""
-------------------------------------------------------
Linked version of the BST ADT.
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-03-16"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _BST_Node:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Initializes a BST node containing value. Child pointers
        are None, height is 1.
        Use: node = _BST_Node(value)
        -------------------------------------------------------
        Parameters:
            value - value for the node (?)
        Returns:
            A _BST_Node object (_BST_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1

    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current node.
        Use: node._update_height()
        -------------------------------------------------------
        Returns:
            _height is 1 plus the maximum of the node's two children.
        -------------------------------------------------------
        """
        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height

        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height

        self._height = max(left_height, right_height) + 1
        return

    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Returns node height and value as a string - for debugging.
        -------------------------------------------------------
        """
        return "h: {}, v: {}".format(self._height, self._value)


class BST:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty BST.
        Use: bst = BST()
        -------------------------------------------------------
        Returns:
            A BST object (BST)
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if bst is empty.
        Use: b = bst.is_empty()
        -------------------------------------------------------
        Returns:
            True if bst is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._root is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of nodes in the BST.
        Use: n = len(bst)
        -------------------------------------------------------
        Returns:
            the number of nodes in the BST.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst. Values may appear
        only once in a tree.
        Use: b = bst.insert(value)
        -------------------------------------------------------
        Parameters:
            value - data to be inserted into the bst (?)
        Returns:
            inserted - True if value is inserted into the BST,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        self._root, inserted = self._insert_aux(self._root, value)
        return inserted

    def _insert_aux(self, node, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst. Values may appear
        only once in a tree.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux(node, value)
        -------------------------------------------------------
        Parameters:
            node - a bst node (_BST_Node)
            value - data to be inserted into the node (?)
        Returns:
            node - the current node (_BST_Node)
            inserted - True if value is inserted into the BST,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        if node is None:
            # Base case: add a new node containing the value.
            node = _BST_Node(value)
            self._count += 1
            inserted = True
        elif value < node._value:
            # General case: check the left subtree.
            node._left, inserted = self._insert_aux(node._left, value)
        elif value > node._value:
            # General case: check the right subtree.
            node._right, inserted = self._insert_aux(node._right, value)
        else:
            # Base case: value is already in the BST.
            inserted = False

        if inserted:
            # Update the node height if any of its children have been changed.
            node._update_height()
        return node, inserted

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in a BST. (Iterative)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value in the node containing key, otherwise None (?)
        -------------------------------------------------------
        """
        node = self._root
        value = None

        while node is not None and value is None:

            if node._value > key:
                node = node._left
            elif node._value < key:
                node = node._right
            elif node._value == key:
                # for comparison counting
                value = deepcopy(node._value)
        return value

    def _remove_aux(self, node, key):
        r = node, None
        if node is None:
            # Key not found
            r = node, None
        else:
            if key < node._value:
                node._left, value = self._remove_aux(node._left, key)
            elif key > node._value:
                node._right, value = self._remove_aux(node._right, key)
            else:  # Found the key
                value = node._value

                # Case 1: Node has no children
                if node._left is None and node._right is None:
                    node = None

                # Case 2: Node has one child
                elif node._left is None:
                    node = node._right
                elif node._right is None:
                    node = node._left

                # Case 3: Node has two children
                else:
                    repl_node = self._delete_node_left(node)
                    # node._value = repl_node._value
                    node._right, _ = self._remove_aux(node._right, repl_node._value)

            if node is not None:
                node._update_height()
            r = node, value
        return r

    def remove(self, key):
        """
        -------------------------------------------------------
        Removes a node with a value matching key from the bst.
        Returns the value matched. Updates structure of bst as
        required.
        Use: value = bst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value matching key if found, otherwise None.
        -------------------------------------------------------
        """
        self._root, value = self._remove_aux(self._root, key)
        return value

    def _delete_node_left(self, parent):
        """
        -------------------------------------------------------
        Finds a replacement node for a node to be removed from the tree.
        Private operation called only by _remove_aux.
        Use: repl_node = self._delete_node_left(node, node._right)
        -------------------------------------------------------
        Parameters:
            parent - node to search for largest value (_BST_Node)
        Returns:
            repl_node - the node that replaces the deleted node. This node
                is the node with the maximum value in the deleted node's left
                subtree (_BST_Node)
        -------------------------------------------------------
        """
        current = parent._left
        while current._right is not None:
            parent = current
            current = current._right
        repl_node = current
        return repl_node

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the bst contains key.
        Use: b = key in bst
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the bst contains key, False otherwise.
        -------------------------------------------------------
        """
        return self._contains_aux(key, self._root)

    def _contains_aux(self, key, node):
        found = False
        if node._value == key:
            found = True
        elif node._left is None and node._right is None:
            found = False
        elif node._left is not None and node._right is not None:
            found = self._contains_aux(key, node._left)
            if found is False:
                found = self._contains_aux(key, node._left)
        elif node._left is not None:
            found = self._contains_aux(key, node._left)
        elif node._right is not None:
            found = self._contains_aux(key, node._right)
        return found

    def height(self):
        """
        -------------------------------------------------------
        Returns the maximum height of a BST, i.e. the length of the
        largest path from root to a leaf node in the tree.
        Use: h = bst.height()
        -------------------------------------------------------
        Returns:
            maximum height of bst (int)
        -------------------------------------------------------
        """

        # your code here


    def _eq_aux(self, node1, node2):
        equals = None
        if node1 is None and node2 is None:
            equals = True
        elif node1 is not None and node2 is not None:
            equals = node1._value == node2._value and \
                self._eq_aux(node1._left, node2._left) and \
                self._eq_aux(node1._right, node2._right)
        else:
            equals = False
        return equals

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two BSTs are equal.
        Values in self and target are compared and if all values are equal
        and in the same location, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a bst (BST)
        Returns:
            equals - True if source contains the same values
                as target in the same location, otherwise False. (boolean)
        -------------------------------------------------------
        """
        return self._eq_aux(self._root, target._root)

    def parent(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node of a key node in a bst.
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found. (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"
        val = None
        parent = self._root

        if parent._value != key:
            if key > parent._value:
                node = parent._right
            else:
                node = parent._left

            while node is not None and val is None:
                if node._value == key:
                    val = deepcopy(parent._value)
                elif key > node._value:
                    parent = node
                    node = node._right
                elif key < node._value:
                    parent = node
                    node = node._left

        return val

    def parent_r(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node in a bst given a key.
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found.
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"
        value = None
        parent = self._root

        if parent._value != key:
            if key > parent._value:
                node = parent._right
            else:
                node = parent._left
            value = self._parent_r_aux(node, parent, key)

        return value

    def _parent_r_aux(self, node, parent, key):
        value = None
        if node is None:
            # base case: value not found
            value = None
        elif node._value == key:
            # base case: value found
            value = deepcopy(parent._value)
        elif key > node._value:
            # node is larger: search right side
            parent = node
            node = node._right
            value = self._parent_r_aux(node, parent, key)
        elif key < node._value:
            # node is smaller: search left side
            parent = node
            node = node._left
            value = self._parent_r_aux(node, parent, key)
        return value

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in BST. (Iterative algorithm)
        Use: value = bst.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"

        # your code here


    def max_r(self):
        """
        ---------------------------------------------------------
        Returns the largest value in a bst. (Recursive algorithm)
        Use: value = bst.max_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"


        # your code here


    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in BST. (Iterative algorithm)
        Use: value = bst.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"
        current = self._root
        while current._left is not None:
            current = current._left
        return deepcopy(current._value)

    def min_r(self):
        """
        ---------------------------------------------------------
        Returns the minimum value in a bst. (Recursive algorithm)
        Use: value = bst.min_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"

        # your code here


    def _leaf_count_helper(self, node):
        r = None
        if node is None:
            r = 0
        elif node._left is None and node._right is None:
            r = 1
        else:
            r = self._leaf_count_helper(node._left) + self._leaf_count_helper(node._right)
        return r

    def leaf_count(self):
        """
        ---------------------------------------------------------
        Returns the number of leaves (nodes with no children) in bst.
        Use: count = bst.leaf_count()
        ---------------------------------------------------------
        Returns:
            count - number of nodes with no children in bst (int)
        ---------------------------------------------------------
        """
        count = self._leaf_count_helper(self._root)
        return count

    def _two_child_count_helper(self, node):
        count = 0
        if node is None:
            pass
        elif node._left is not None and node._right is not None:
            count += 1
            count += self._two_child_count_helper(node._left)
            count += self._two_child_count_helper(node._right)
        return count

    def two_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.two_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with two children in bst (int)
        ----------------------------------------------------------
        """
        count = self._two_child_count_helper(self._root)
        return count

    def _one_child_count_helper(self, node):
        count = 0
        if node is None:
            pass
        elif (node._left is not None and node._right is None) or \
            (node._left is None and node._right is not None):
            count += 1
            count += self._one_child_count_helper(node._left)
            count += self._one_child_count_helper(node._right)
        return count

    def one_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.one_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with one child in bst (int)
        ----------------------------------------------------------
        """
        count = self._one_child_count_helper(self._root)
        return count

    def node_counts(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: zero, one, two = bst.node_counts()
        -------------------------------------------------------
        Returns:
            zero - number of nodes with zero children (int)
            one - number of nodes with one child (int)
            two - number of nodes with two children (int)
        ----------------------------------------------------------
        """
        zero = 0
        one = 0
        two = 0

        node = self._root
        zero, one, two = self._node_counts_aux(node, zero, one, two)
        return zero, one, two

    def _node_counts_aux(self, node, zero, one, two):
            if node is None:
                # case empty list
                pass
            elif node._left is None and node._right is None:
                # case zero children
                zero += 1
            elif node._left is None:
                # case one child
                one += 1
                zero, one, two = self._node_counts_aux(node._right, zero, one, two)
            elif node._right is None:
                # case one child (opposite direction)
                one += 1
                zero, one, two = self._node_counts_aux(node._left, zero, one, two)
            else:
                # case two children
                two += 1
                zero, one, two = self._node_counts_aux(node._left, zero, one, two)
                zero, one, two = self._node_counts_aux(node._right, zero, one, two)

            return zero, one, two

    def _subtree_depth(self, node):
        n = 0
        ld = 0
        rd = 0
        if node is not None:
            n += 1
            ld = self._subtree_depth(node._left)
            rd = self._subtree_depth(node._right)
        n += rd > ld and rd or ld
        return n

    def is_balanced(self):
        """
        ---------------------------------------------------------
        Returns whether a bst is balanced, i.e. the difference in
        height between all the bst's node's left and right subtrees is <= 1.
        Use: b = bst.is_balanced()
        ---------------------------------------------------------
        Returns:
            balanced - True if the bst is balanced, False otherwise (boolean)
        ---------------------------------------------------------
        """
        balanced = True
        if self._root is not None:
            ld = self._subtree_depth(self._root._left)
            rd = self._subtree_depth(self._root._right)
            balanced = abs(ld - rd) <= 1
        return balanced

    def _node_height(self, node):
        """
        ---------------------------------------------------------
        Helper function to determine the height of node - handles empty node.
        Private operation called only by _is_valid_aux.
        Use: h = self._node_height(node)
        ---------------------------------------------------------
        Parameters:
            node - the node to get the height of (_BST_Node)
        Returns:
            height - 0 if node is None, node._height otherwise (int)
        ---------------------------------------------------------
        """
        if node is None:
            height = 0
        else:
            height = node._height
        return height

    def retrieve_r(self, key):
        """
        -------------------------------------------------------
        Retrieves a _value in a BST. (Recursive)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - If bst contains key, returns value, else returns None.
        -------------------------------------------------------
        """

        # your code here


    def _height(self, node):
        h = 0
        if node is not None:
            h = node._height
        return h

    def _is_valid_helper(self, node, min_val, max_val):
        r = None
        if node is None:
            r = True
        elif not min_val < node._value < max_val:
            r = False
        elif not self._is_valid_helper(node._left, min_val, node._value):
            r = False
        elif not self._is_valid_helper(node._right, node._value, max_val):
            r = False
        else:
            r = node._height == 1 + max(self._height(node._left), self._height(node._right))
        return r

    def is_valid(self):
        """
        ---------------------------------------------------------
        Determines if a tree is a valid BST, i.e. the values in all left nodes
        are smaller than their parent, and the values in all right nodes are
        larger than their parent, and height of any node is 1 + max height of
        its children.
        Use: b = bst.is_valid()
        ---------------------------------------------------------
        Returns:
            valid - True if tree is a BST, False otherwise (boolean)
        ---------------------------------------------------------
        """
        valid = False
        if self._root is None:
            valid = True
        else:
            valid = self._is_valid_helper(self._root, float("-inf"), float("inf"))
        return valid

    def _inorder_helper(self, node, result):
        if node is not None:
            self._inorder_helper(node._left, result)
            result.append(deepcopy(node._value))
            self._inorder_helper(node._right, result)

    def inorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in inorder order.
        Use: a = bst.inorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in inorder (list of ?)
        -------------------------------------------------------
        """
        result = []
        self._inorder_helper(self._root, result)
        return deepcopy(result)

    def _preorder_helper(self, node, result):
        if node is not None:
            result.append(deepcopy(node._value))
            self._preorder_helper(node._left, result)
            self._preorder_helper(node._right, result)

    def preorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in preorder order.
        Use: a = bst.preorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in preorder (list of ?)
        -------------------------------------------------------
        """
        result = []
        self._preorder_helper(self._root, result)
        return deepcopy(result)

    def _postorder_helper(self, node, result):
        if node is not None:
            self._postorder_helper(node._left, result)
            self._postorder_helper(node._right, result)
            result.append(deepcopy(node._value))

    def postorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in postorder order.
        Use: a = bst.postorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in postorder (list of ?)
        -------------------------------------------------------
        """
        result = []
        self._postorder_helper(self._root, result)
        return deepcopy(result)

    def levelorder(self):
        """
        -------------------------------------------------------
        Copies the contents of the tree in levelorder order to a list.
        Use: values = bst.levelorder()
        -------------------------------------------------------
        Returns:
            values - a list containing the values of bst in levelorder.
            (list of ?)
        -------------------------------------------------------
        """
        result = []
        if self._root is not None:
            queue = []
            queue.append(self._root)
            while len(queue) > 0:
                node = queue.pop(0)
                result.append(deepcopy(node._value))
                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)
        return result

    def count(self):
        """
        ---------------------------------------------------------
        Returns the number of nodes in a BST.
        Use: number = bst.count()
        -------------------------------------------------------
        Returns:
            number - count of nodes in tree (int)
        ----------------------------------------------------------
        """

        # your code here


    def __iter__(self):
        """
        -------------------------------------------------------
        Generates a Python iterator. Iterates through a BST node
        in level order.
        Use: for v in bst:
        -------------------------------------------------------
        Returns:
            yields
            value - the values in the BST node and its children (?)
        -------------------------------------------------------
        """
        if self._root is not None:
            # Put the nodes for one level into a queue.
            queue = []
            queue.append(self._root)

            while len(queue) > 0:
                # Add a copy of the data to the sublist
                node = queue.pop(0)
                yield node._value

                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)
