class StackLinkedList:
    """Implements an efficient last-in first-out Abstract Data Type using a linked List"""

    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None

    def __init__(self, capacity):
        """Creates and empty stack with a capacity"""
        self.capacity = capacity  # Capacity of your stack
        self.head = None  # expect an instance of type Node - This is the starting point of the linked list
        self.num_items = 0  # number of elements in the stack

    def is_empty(self):
        """Returns true if the stack self is empty and false otherwise"""
        return self.num_items == 0

    def is_full(self):
        """Returns true if the stack self is full and false otherwise"""
        return self.capacity == self.num_items
    def push(self, item):
        """Adds item to the stack"""
        if self.is_full():
            raise IndexError('Its full')
        new_node = self.Node(item)
        new_node.next = self.head
        self.head = new_node
        self.num_items = 1 + self.num_items


    def pop(self):
        """Returns the current top of the stack"""
        if self.is_empty():
            raise IndexError('Its empty')
        pooop = self.head
        self.head = self.head.next
        self.num_items = self.num_items - 1
        return pooop

    def peek(self):
        """Returns the value of the item at the top of the stack without removing it"""
        return self.head.item
    def size(self):
        """Returns the number of elements currently in the stack, not the capacity"""
        return self.num_items
