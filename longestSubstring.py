class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
      maximum = 0

    # Input: s = "abcabcbb"
    # Output: 3  
      
      #sliding window
      a_pointer = 0
      b_pointer = 0 #moves til the end til it finds duplicate
      #when a duplicate is found, a_pointer is moved

      unique = set() #holds all unique consecutive characters

      while b_pointer < len(s):
          if s[b_pointer] not in unique:

              unique.add(s[b_pointer])
              #add max since a unique ch is found
              b_pointer += 1
              maximum = max(maximum, len(unique)) 

          else:
              #remove ch at a_pointer from set (to slide the window) then increment a_pointer
              unique.remove(s[a_pointer])
              a_pointer += 1


      return maximum