# Given two arrays of integers nums and index. 
# Your task is to create target array under the following rules:

# Initially target array is empty.
# From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
# Repeat the previous step until there are no elements to read in nums and index.
# Return the target array.

class Solution:
    def createTargetArray(self, nums, index):
        target_array = []
        pointer = 0
        #use .insert(index, element): it inserts element in a desired index, and shifts the rest of the element
        for i in nums:
            target_array.insert(index[pointer], i)
            # target[index[pointer]]
            pointer += 1

        return target_array

nums = [0,1,2,3,4]
index = [0,1,2,2,1]

s1 = Solution()

print(s1.createTargetArray(nums, index))