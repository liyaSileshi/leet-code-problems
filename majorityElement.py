#Given an array of size n, find the majority element. 
# The majority element is the element that appears more than ⌊ n/2 ⌋ 
# times.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # len(nums) // 2
        #create a histogram of counts
        # loop and check which one has a count morethan len(nums) // 2
        major = len(nums) // 2
        nums_hist = {}
        for num in nums:
            if num in nums_hist:
                nums_hist[num] += 1
            else:
                nums_hist[num] = 1
        for key, value in nums_hist.items():
            if value > major:
                return key