# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def hasCycle(self, head: ListNode) -> bool:
        '''
        Approach 1: set
        Time complexity: O(n)
        Space complexity: O(n)
        '''
        # list_set = set()
        # curr = head
        # while curr != None:
        #     #check if the memory adress of curr is in set
        #     if curr in list_set:
        #         return True
        #     list_set.add(curr)
        #     #increment current
        #     curr = curr.next
        # return False 
    
        '''
        Approach 2: slow and fast pointer
        Time complexity: O(fast)
        Space complexity: O(1)
        '''
        if head == None:
            return False
        #initialize fast and slow to head
        slow = head
        fast = head.next
        while slow != fast:
            if fast==None or fast.next==None:
                return False #fast reached the end
            #make them run
            slow = slow.next
            fast = fast.next.next
        return True #they're equal (cycle)