# Subtract the Product and Sum of Digits of an Integer
# Given an integer number n, return the difference between 
# the product of its digits and the sum of its digits.


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        #initialize add and product variable
        add = 0
        product = 1 #product is set to one b/c 1*any number is itself
        #change the int to string and iterate through the characters
        for i in str(n):
            #add and multiply
            add += int(i)
            product *= int(i)
        #return the difference
        return product - add