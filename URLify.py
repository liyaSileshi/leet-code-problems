'''
Write a method to replace all the spaces in a string with ‘%20’. 
You may assume that the string has sufficient space at the end to 
hold the additional characters, and that you are given the “true” 
length of the string.
'''
#loop over input
#if u see a whitespace, change to %20

def urlify(word, num):
  # convert to list
  wordList = list(word)
  # loop over wordlist
  for i in range(num):
    if wordList[i] == ' ':
      wordList[i] = '%20'
  # join the list to form a string
  word = ''.join(wordList)
  print(word)
  return word
urlify('Mr John Smith   ', 13)
