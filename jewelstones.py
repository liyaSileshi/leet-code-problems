# You're given strings J representing the types of stones
# that are jewels, and S representing the stones you have.
# Each character in S is a type of stone you have.  
# You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, 
# and all characters in J and S are letters. 
# Letters are case sensitive, so "a" is considered 
# a different type of stone from "A".

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = 0
        for i in S:
            if i in J:
                counter += 1
        return counter
    
s1 = Solution()
print(s1.numJewelsInStones('z', "ZZ"))
