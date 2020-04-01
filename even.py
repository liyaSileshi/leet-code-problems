#Find Numbers with Even Number of Digits
# Given an array nums of integers, 
# return how many of them contain an even number of digits.

#1, Restate the problem
#    - So I am asked to find the total amount of numbers given in an array,
#       that have even number of digits?

#2, Ask clarifying questions
#   - Do I return the total count of numbers that have even number of digits,
#     or do I return the numbers in a list?
#   - Could there be negative numbers?

#3, Assumptions
#   - Return the total count
#   - Negative numbers could be included


class Solution:
    def findNumbers(self, nums):
        #have a count variable
        count = 0
        # loop through the array
        for num in nums:
            #check the length of each number
            #convert to string and find the length of the string
            #if it's even, increment count
            if len(str(num)) % 2 == 0:
                count += 1
        #return the count
        return count
    

if __name__ == '__main__':
    s1 = Solution()
    print(s1.findNumbers([555,901,482,1771]))