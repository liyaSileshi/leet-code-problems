# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes
#  of the first two lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #pointers for both list nodes
        p1 = l1
        p2 = l2
        
        if p1 == None and p2 == None:
            return p1
        if p1 != None and p2 == None:
            new_ll = ListNode(p1.val)
            p1 = p1.next
            #pointer for the new ll
            new_p = new_ll
            while p1 != None:
                #loop over the rest
                node = ListNode(p1.val)
                new_p.next = node
                p1 = p1.next
                new_p = new_p.next
            return new_ll
        if p2 != None and p1 == None:
            new_ll = ListNode(p2.val)
            p2 = p2.next
            #pointer for the new ll
            new_p = new_ll
            while p2 != None:
                #loop over the rest
                node = ListNode(p2.val)
                new_p.next = node
                p2 = p2.next
                new_p = new_p.next
            return new_ll
            
        #compare value of the pointers
        if p1.val <= p2.val:
            #new linked list
            new_ll = ListNode(p1.val)
            #move p1
            p1 = p1.next
        else:
            new_ll = ListNode(p2.val)
            p2 = p2.next
            
        #pointer for the new ll
        new_p = new_ll
        while (p1 != None and p2 != None):
            if p1.val <= p2.val:
                node = ListNode(p1.val)
                new_p.next = node
                #move p1
                p1 = p1.next
                #move newp
                new_p = new_p.next
            else:
                node = ListNode(p2.val)
                new_p.next = node
                p2 = p2.next
                new_p = new_p.next
        #check which list is left with nodes
        if p1 != None:
            while p1 != None:
                #loop over the rest
                node = ListNode(p1.val)
                new_p.next = node
                p1 = p1.next
                new_p = new_p.next
        if p2 != None:
            while p2 != None:
                #loop over the rest
                node = ListNode(p2.val)
                new_p.next = node
                p2 = p2.next
                new_p = new_p.next
                
        return new_ll
        