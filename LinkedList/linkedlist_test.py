#!python

from linkedlist import LinkedList, Node
import unittest


class NodeTest(unittest.TestCase):

    def test_init(self):
        data = 'ABC'
        node = Node(data)
        # Initializer should add instance properties
        assert node.data is data
        assert node.next is None

    def test_linking_nodes(self):
        node1 = Node('A')
        node2 = Node('B')
        node3 = Node('C')
        # Link nodes together
        node1.next = node2
        node2.next = node3
        # Node links should be transitive
        assert node1.next is node2  # One link
        assert node1.next.next is node3  # Two links


class LinkedListTest(unittest.TestCase):

    def test_init(self):
        ll = LinkedList()
        # Initializer should add instance properties
        assert ll.head is None  # First node
        assert ll.tail is None  # Last node

    def test_init_with_list(self):
        ll = LinkedList(['A', 'B', 'C'])
        # Initializer should append items in order
        assert ll.head.data == 'A'  # First item
        assert ll.tail.data == 'C'  # Last item

    def test_items_after_append(self):
        ll = LinkedList()
        assert ll.items() == []
        # Append should add new item to tail of list
        ll.append('A')
        assert ll.items() == ['A']
        ll.append('B')
        assert ll.items() == ['A', 'B']
        ll.append('C')
        assert ll.items() == ['A', 'B', 'C']


    def test_append(self):
        ll = LinkedList()
        # Append should always update tail node
        ll.append('A')
        assert ll.head.data == 'A'  # New head
        assert ll.tail.data == 'A'  # New tail
        ll.append('B')
        assert ll.head.data == 'A'  # Unchanged
        assert ll.tail.data == 'B'  # New tail
        ll.append('C')
        assert ll.head.data == 'A'  # Unchanged
        assert ll.tail.data == 'C'  # New tail


    def test_find(self):
        ll = LinkedList(['A', 'B', 'C'])
        assert ll.find('B') == 'B'  # Match equality
        assert ll.find('C') == 'C'  # Match equality
        assert ll.find('X') is None  # No matching item

    def test_delete(self):
        ll = LinkedList(['A', 'B', 'C'])
        assert ll.head.data == 'A'  # First item
        assert ll.tail.data == 'C'  # Last item
        ll.delete_from_tail() #more than one item
        assert ll.head.data == 'A'  
        assert ll.tail.data == 'B'  
        ll.delete_from_tail() #more than one item
        assert ll.head.data == 'A' 
        assert ll.tail.data == 'A'  
        ll.delete_from_tail() #one item
        assert ll.head is None  # No head
        assert ll.tail is None  # No tail
        ll.delete_from_tail() #empty list
        assert ll.head is None  # No head
        assert ll.tail is None  # No tail


if __name__ == '__main__':
    unittest.main()