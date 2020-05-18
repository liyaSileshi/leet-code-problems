# Given a string s and a non-empty string p, find all the start indices
#  of p's anagrams in s.

# Strings consists of lowercase English letters only and the 
# length of both strings s and p will not be larger than 20,100.
# The order of output does not matter.

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagram_arr = []
        #sort p
        p_list = sorted(p)
        p = ''.join(p_list)

        #loop over s-substirng
        for i in range(len(s)-len(p)+1):
            #create the substring
            sub = s[i:i+len(p)]
            #sort the sublist
            sub_list = sorted(sub)
            sub = ''.join(sub_list)
            #check if it's equal with p
            if sub == p:
                anagram_arr.append(i)
   
        return anagram_arr
            