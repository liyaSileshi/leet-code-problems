# In a array A of size 2N, there are N+1 unique elements, 
# and exactly one of these elements is repeated N times.
# Return the element repeated N times.

class Solution:
    def repeatedNTimes(self, A):
        #create a dictionary to store all the unique nums 
        #keys would be num and value True/False based of uniqueness
        unique_num = dict()
        for num in A:
            if num in unique_num:
                unique_num[num] = False
                return num
            else:
                unique_num[num] = True

s1 = Solution()
print(s1.repeatedNTimes([5,1,5,2,5,3,5,4]))