#!/usr/bin/python3

"""Module defines a node of a singly linked list"""


class Node:
    """Node structure for singly linked lists"""
    def __init__(self, data, next_node=None):
        """initializing node members
        Args:
            data: data per node
            next_node: guide to next node
         """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        return the value of data property
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        params:
            Value (int): new value
        resets the data property of a function
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """
        function to return next node
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        resets the value to th next_node
        params:
            value (Node): new node to point to
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """creation of singly linked list"""
    def __init__(self):
        """head of the nodes"""
        self.head = None

    def sorted_insert(self, value):
        """
        function to insert node in sorted manner
        param:
            value (Node): new node to insert
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return
        current_node = self.head
        while (current_node.next_node is not None) and
        (current_node.next_node.data < value):
            current_node = current_node.next_node
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    def __str__(self):
        """string rep of the square value"""
        nodes = []
        current_node = self.head
        while current_node is not None:
            nodes.append(str(current_node.data))
            current_node = current_node.next_node
        return "\n".join(nodes)
