#!/usr/bin/python3
"""
Module to define nodes
"""


class Node:
    """
    defines a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        get the value of data property
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        resets the value of data property
        Params:
            value(int): new value
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        get the value of next_node property
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        resets the value of next_node property
        Params:
            value(int): new value
        """
        if value is not None and not isinstance(value, self.__class__):
            raise ValueError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """
    Class defining the base singely linked list structure
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """
        inserts a new Node into the correct
        sorted position in the list (increasing order)

        params:
            value (Node): value to use to create new node
        """
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
            return

        # else find its correct position

        prev = None
        curr = self.__head

        while curr is not None:
            if curr.data > value:
                if prev is not None:  # curr is not self.__head
                    prev.next_node = new_node
                else:
                    self.__head = new_node
                new_node.next_node = curr
                return
            prev = curr
            curr = curr.next_node

        # place new_node at the end
        prev.next_node = new_node

    def __str__(self):
        """
        computes the printable representation of the list
        one node number by line
        """
        data = []
        trav = self.__head

        while trav is not None:
            data.append(str(trav.data))
            trav = trav.next_node

        return "\n".join(data)
