#Given a positive integer, output its complement 
# number. The complement strategy is to flip the 
# bits of its binary representation.

# Input: 5
# Output: 2
# Explanation: The binary representation of 5 
# is 101 (no leading zero bits), and its 
# complement is 010. So you need to output 2.

def findComplement(num):
    #Time complexity:
    #Space complexity:
    #convert digit to binary
    to_base = ''
    while num >= 2:
        (quo, mod) = (num // 2, num % 2)
        to_base = str(mod ^ 1) + to_base
        num = quo

    to_base = str(quo ^ 1) + to_base # the last quotient
    power, digit = len(to_base)-1 , 0
    for char in to_base:
        digit += (2**power) * int(char)
        power -= 1

    return digit
findComplement(2)