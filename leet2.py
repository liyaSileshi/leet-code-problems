# Given a 32-bit signed integer, reverse digits of an integer.
input = 123
class Solution:
    def reverse(self, x: int) -> int:
        new_list = []
        digit_list = [int(x) for x in str(input)]
        while(len(digit_list) > 0):
            new_list.append(digit_list[-1])
            digit_list = digit_list[:-1]
            s = [str(x) for x in new_list]
            res = int("".join(s))
        return res

r1 = Solution()
print(r1.reverse(input))