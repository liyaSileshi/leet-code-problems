'''
19. Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        Approach 1: Two pass algorithm
        '''
#         if head == None: #empty linked list
#             return head
  
#         #find the length
#         length = 1
#         curr = head
#         while curr.next != None:
#             curr = curr.next
#             length += 1
        
#         #if removing head
#         if length - n == 0:
#             head = head.next
#             return head
        
#         #find length - n
#         start = 1
#         curr = head
#         #once start is equal to length - n: we find the node before target
#         while start < length - n and curr.next != None:
#             #advance curr
#             curr = curr.next
#             start += 1
            
#         rem = curr.next
#         #change curr pointer to next.next
#         curr.next = curr.next.next
#         rem.next = None
        
#         return head
    
        '''
        Approach 2: One pass algorithm
        '''
        #have a dummy node from where both first and second start
        dummy =  ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        #make them n first pointer and second pointer n node apart
        for i in range(n+1):
            print(first)
            first = first.next
            
        #move both first and second pointer
        while first != None:
            first = first.next
            second = second.next
            
        #move second next (to not point to target)
        second.next = second.next.next
        
        return dummy.next