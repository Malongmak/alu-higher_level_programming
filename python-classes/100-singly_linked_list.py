#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        values = []
        current_node = self.head
        while current_node:
            values.append(str(current_node.data))
            current_node = current_node.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return
        current_node = self.head
        while current_node.next_node is not None and current_node.next_node.data < value:
            current_node = current_node.next_node
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
