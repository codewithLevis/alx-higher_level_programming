#!/usr/bin/python3
"""A linked list module"""


class Node:
    """Node structure"""
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
        """getter of data"""
        return(self._data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """getter of next_node"""
        return(self._next_node)

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """creation of singly linked list"""
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        """method sorting the list"""
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
        nodes = []
        current_node = self.head
        while current_node is not None:
            nodes.append(str(current_node.data))
            current_node = current_node.next_node
        return "\n".join(nodes)