# Finding the closing paranthesis for a given opening parenthesis
word = '(a(b)(d(e)))f(g)'
myStack = []

def findPair(string, target):
    for i in range(len(string)):
        if string[i] == '(':
            myStack.append(i)
        elif string[i] == ')':
            name = myStack.pop()
            if name == target:
                return i
        
print(findPair(word, 0))
