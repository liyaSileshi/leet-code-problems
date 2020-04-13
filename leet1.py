nums = [-3, -4, 3, 90]
target = 0                                                   
class Solution:
    def twoSum(self, nums, target: int):
        newArr = []
        for i in range(len(nums)):
            if abs(nums[i]) <= abs(target) or abs(nums[i]) in nums:
                newArr.append(nums[i])

        for i in range(len(nums)):
            if nums[i] in newArr:
                for j in range(len(nums)):
                    if nums[j] in newArr:
                        if i!=j and nums[i]+nums[j] == target:
                            return [i,j]

        # for i in range(len(nums)):
        #     # if nums[i] <= target or abs(nums[i]) in nums :
        #     for j in range(len(nums)):
        #             # if nums[j] <= target or abs(nums[j]) in nums:
        #         if i != j and nums[i]+nums[j] == target:
        #             return [i,j]
l1= Solution()
print(l1.twoSum(nums, target))