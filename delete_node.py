# Write a function to delete a node (except the tail) 
# in a singly linked list, given only access to that node.

# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place                   instead.
        """
        node.val = node.next.val #copy the value of next into current
        #delete the next
        next_val = node.next #store the next val in a variable
        node.next = node.next.next #change the link of current
        next_val.next = None#delete next
        