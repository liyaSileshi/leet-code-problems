class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        size = len(num)
        if k == size:
            return '0'
        
        pointer = 0
        stack = []
        #check if pointer is not out of bounds
        while pointer < size:
            while k>0 and len(stack) != 0 and stack[-1] > num[pointer]:
                stack.pop()
                k -= 1 #decrement because we removed an elt
            stack.append(num[pointer])
            pointer += 1
         
        #if all characters are the same
        #delete k elts
        while k > 0:
            stack.pop()
            k -= 1
        
        # removing zeros at front
        while stack[0] == '0' and len(stack) > 1:
            stack.pop(0)
        
        
        strStack = ''.join(stack)
        return strStack