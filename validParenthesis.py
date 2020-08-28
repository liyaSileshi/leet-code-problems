def valid(expression):
  stack = []
  #loop throught the expression
  for ele in expression:
    #if ele is (, { or [
    if ele == "{" or ele == "(" or ele == "[":
      #append to stack
      stack.append(ele)
    #if ele is ), } or ]
    elif ele == "}" or ele == ")" or ele == "]":
      #if the stack is empty
      if len(stack) == 0:
        return 0
      #if ele does not have cooresponding opening at the top of stack
      elif ele == '}' and stack[-1] != "{":
        return 0
      elif ele == ')' and stack[-1] != "(":
        return 0
      elif ele == ']' and stack[-1] != "[":
        return 0
      #if it has a match at the top of the stack
      elif ele == '}' and stack[-1] == "{":
        stack.pop()
      elif ele == ']' and stack[-1] == "[":
        stack.pop()  
      elif ele == ')' and stack[-1] == "(":
        stack.pop()
      
  if len(stack) == 0:
    return 1
  return 0

expression = "()"
print(valid(expression))
