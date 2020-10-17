'''
242. Valid Anagram
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Time complexity: O(n): 
        Space complexity: O(n): making the hashtable
        '''  
        if len(s) != len(t):
            return False
        
        #make hashtable for string s
        hash_s = {}
        for ch in s:
            if ch in hash_s:
                hash_s[ch] += 1
            else:
                hash_s[ch] = 1
        
        #loop through t and decrement value
        #as you loop, check if the value gets lower than 0
        #if it is, it's not anagram
        for ch in t:
            if ch in hash_s:
                hash_s[ch] -= 1
                #as you loop, check if the value gets lower than 0
                if hash_s[ch] < 0:
                    return False
            else:
                #not anagram
                return False
        return True