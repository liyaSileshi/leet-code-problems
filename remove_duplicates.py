class Solution:
  def removeDuplicates(self, s: str) -> str:
    #clarifying qns
    #what abt special characters or uppercase?
    
    # if it's only one letter, ? return it 
    
    # "abbaca"
    #     ^
    
    #use stack concept
    i = 0
    stack = []
    
    while i < len(s):
        if len(stack) == 0:
            stack.append(s[i])
            #Increment i
            i += 1
        #check top of stack with curr ele
        elif stack[-1] == s[i]:
            #remove ele from stack
            stack.pop(-1)
            #increment i
            i += 1
        else:
            #append in stack
            stack.append(s[i])
            #increment i
            i += 1
    return ''.join(stack)
  