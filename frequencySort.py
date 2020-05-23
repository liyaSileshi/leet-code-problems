# Given a string, sort it in decreasing order 
# based on the frequency of characters.
# Input:
# "tree"
# Output:
# "eert"

class Solution:
    def frequencySort(self, s: str) -> str:
        #make a hashtable
        hash_str = {}
        for i in s:
            if i in hash_str.keys():
                hash_str[i] += 1
            else:
                hash_str[i] = 1
        #sort by value in descending order
        hash_str = {k:v for k, v in sorted(hash_str.items(), key=lambda item:item[1], reverse=True)}
        
        #loop through dict and append to a string
        output = ''
        for key, value in hash_str.items():
            while value > 0:
                output += key
                #decrement value
                value -= 1
        return output
        