# find permutation
# check if it's a palindrome

# for each pemutation, check if it's a palindrome

# strings with an even length, must have even count
# all their character
# strings with odd length, have only 1 character that has
# 1 count. the rest is even count

#clarifying qns: do white spaces matter
#do other symbols matter
#is a num also counted
#is it case sensetive or not?


# METHOD 1: using a histogram - hashtable
#case insensetive
#numbers count
#white spaces don't matter
def palindromePermutation(word):
  '''
    Time Complexity: O(n)
  '''
  #make a histogram for the word using a hashtable
  hist_word = {}
  countOdd = 0
  for ch in word:
    #if it's a num or alpha
    if ch.isalnum():
      if ch.lower() in hist_word:
        hist_word[ch.lower()] += 1
      else:
        hist_word[ch.lower()] = 1
      # to keep track of how many odds we have
      if hist_word[ch.lower()] % 2 == 0:
        countOdd -= 1
      else: 
        countOdd += 1
  return countOdd <= 1

print(palindromePermutation('Tact Coa'))
print(palindromePermutation('lliyy'))

# METHOD 2: using bitwise operation
def bitPalindromePermutation(word):
