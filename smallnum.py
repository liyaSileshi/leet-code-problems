# Given the array nums, for each nums[i] find out
# how many numbers in the array are smaller than it.
# That is, for each nums[i] you have to count the number 
# of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        #have a pointer that points to current num we're looking at
        pointer = 0
        lst2 = []
        counter = 0
        #loop through the list for each num we look at
        while pointer < len(nums):
            for i in nums:
                if nums[pointer] > i:
                    counter +=1

            lst2.append(counter)
            counter = 0 #reinitialize counter
            pointer += 1
        return lst2
        #compare it with current num
        #if it's less, increment counter
        #append counter at the end to a new list

s1 = Solution()
print(s1.smallerNumbersThanCurrent([7,7,7,7]))
