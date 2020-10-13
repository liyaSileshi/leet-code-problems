class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #create a hash_table key- nums value- index
        num_hash = {}
        for i in range(len(nums)):
            value = nums[i]
            #assign index as value to each nums hash
            num_hash[value] = i
               
        for i in range(len(nums)):
            value = target - nums[i]
            if value in num_hash and num_hash[value] != i:
                return [i, num_hash[value]]
        