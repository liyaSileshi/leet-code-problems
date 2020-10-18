  #Question 
#Reverse a singly linked list.
#Input: 1->2->3->4->5->NULL
#Output: 5->4->3->2->1->NULL

#1, Restate the problem
#   So given a linked list, I am asked to reverse the 
#   entire list? 

#2, Ask clarifying questions
#   Can I modify the given list or do I need to create another linked list?
#   Is the list in ascending/descending order?
#   Are the values sorted?
#   Are we dealing with smaller input or could it be large?

#3, Assumptions
#   You can either modify the given list or create another one
#   The list is not in any order
#   The list could be of any size

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#Solution 1
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        temp = [] #create a list to hold all the items in the ll
        #reach the end of the node
        while head:
            temp.insert(0, head.val) #to prepend items from the ll
            head = head.next 
        if len(temp) == 0: #no node (edge case)
            return head #return the same thing
        
        node1 = ListNode(temp[0]) #first node
        pointer = node1 #pointer starts at first node
        
        for i in range(1, len(temp)): #loop through the list starting from second index
                node = ListNode(temp[i]) #create a node holding the i'th value
                pointer.next = node # connect it with the other nodes(where the current pointer is)
                pointer = pointer.next #change pointer to the next node
        return node1


#Solution 2 - faster runtime and modifies the given ll instead of making a new one
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         #create a previous and current pointer variable
#         prev = None
#         curr = head
        
#         while curr != None: #starts from the first node
#             next_curr = curr.next #put curr.next into a variable before updating it
#             curr.next = prev #to point backwards (to the node on it's left)
#             prev = curr #shift previous pointer to the right
#             curr = next_curr #shift curr to right
            
#         return prev
    

# if __name__ == '__main__':
#     s1 = Solution()
#     s1.reverseList([1])

