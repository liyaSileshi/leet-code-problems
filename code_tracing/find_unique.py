# Given a non-empty array of integers, 
# every element appears twice except for
# one. Find that single one.
# Input: [4,1,2,1,2]
# Output: 4

# variable : value
# nums     : [4, 1, 2, 1, 2]
#hash_num  :  {4: True, 1:False, 2: False}
# i : 2
#key : 4
#value : True

class Solution:
    def singleNumber(self, nums) -> int:
        hash_num = {}
        #put the array in hashtable, key is nums: value is boolean
        for i in nums:
            if i in hash_num:
                hash_num[i] = False
            else:
                hash_num[i] = True
        #iterate through hashtable value
        for key, value in hash_num.items():
            if value == True: #not duplicate
                return key

if __name__ == '__main__':
    s1 = Solution()
    print(s1.singleNumber([4,1,2,1,2]))