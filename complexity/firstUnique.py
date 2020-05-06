#Given a string, find the first non-repeating 
# character in it and return it's index. If it 
# doesn't exist, return -1.


class Solution:
    #Time complexity: O(n) - making the histogram
    #Space complexity: O(n) - making the histogram
    def firstUniqChar(self, s: str) -> int:
        #create a histogram
        count_s = {}
        for ch in s:
            if ch in count_s:
                count_s[ch] += 1
            else:
                count_s[ch] = 1
                
        #loop over the string
        for index, ch in enumerate(s):
            if count_s[ch] == 1:
                return index
        #it doesn't exist
        return -1