# Given an array nums, write a function to move all 0's 
# to the end of it while maintaining the relative order 
# of the non-zero elements.

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        for i in range(len(nums)):
            if nums[i] != 0: #if element not zero
                #shift to the left the non-zero and swap with zero
                nums[i], nums[pointer] = nums[pointer], nums[i]
                pointer += 1 #increment pointer

            
nums = [0,0,1]
s1 = Solution()
s1.moveZeroes(nums)
print(nums)

        