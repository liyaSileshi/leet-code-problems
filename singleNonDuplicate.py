# You are given a sorted array consisting of only integers where every 
# element appears exactly twice, except for one element which appears 
# exactly once. Find this single element that appears only once.

# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        pointer = 0
        while pointer < (len(nums) - 2):
            if nums[pointer] == nums[pointer+1]:
                #skip the next
                pointer += 2
            else:
                return nums[pointer]
            
        #last elt has no duplicate
        return nums[-1]
