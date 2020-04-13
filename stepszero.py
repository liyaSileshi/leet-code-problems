# Given a non-negative integer num,
# return the number of steps to reduce it to zero.
# If the current number is even, you have to divide
# it by 2, otherwise, you have to subtract 1 from it

class Solution:
    def numberOfSteps (self, num: int):
        counter = 0
        curr = num
        while curr != 0:
            if curr % 2 == 0:
                curr = curr/2      
            else:
                curr -= 1
            counter += 1
        return counter

s1 = Solution()
print(s1.numberOfSteps(123))