# Given head which is a reference node to a singly-linked list.
# The value of each node in the linked list is either 0 or 1. 
# The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        #create a variable to store the length of the linkedlist
        count_length = 0
        count_pointer = head
        #make another pointer for the length counter
        while count_pointer != None:
            #increment until there's no more node
            count_length += 1
            count_pointer = count_pointer.next


        val = 0
        #pointer gives the value of the power which 2 is raised by
        #to convert to decimal
        pointer = count_length - 1
        #while there is still a node
        while head != None:
            val += (head.val * (2**pointer))  
            pointer -= 1
            head = head.next
            
        return val
