#!python


class Node:

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list of items stored in the linked list."""
        items = []
        current = self.head
        while current != None:
            items.append(current.data)
            current = current.next
        return items

    def append(self, item):
        """Insert the given item at the tail of this linked list."""
        new_node = Node(item)
        if self.tail is not None:
            self.tail.next = new_node
        if self.head is None:
            self.head = new_node
        self.tail = new_node


    def find(self, item):
        """Return an item from this linked list satisfying the given quality."""
        current = self.head
        while current.next != None:
            if current.data == item:
                return current
            current = current.next


    def delete_from_tail(self):
        """Delete the last item of this linked list if not empty."""

        current = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        #get the node right before the tail
        while current != None:
            if current.next == self.tail:
                current.next = None
                self.tail = current

                
                return
            current = current.next