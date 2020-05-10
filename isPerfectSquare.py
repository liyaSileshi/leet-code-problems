# Given a positive integer num, write a 
# function which returns True if num is a 
# perfect square else False.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        #calculate sqrt
        root = num**(1/2)
        #substract to get decimal point
        dec = root - int(root)
        if dec == 0.0:
            return True
        return False