#Write a program that outputs the string representation of numbers from 1 to n.
#But for multiples of three it should output “Fizz”
#instead of the number and for the multiples of five output “Buzz”.
# For numbers which are multiples of both three and five output “FizzBuzz”.

class Solution:
    def fizzBuzz(self, n: int):
        output = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                output.append('FizzBuzz')
            elif i % 3 == 0:
                output.append('Fizz')
            elif i % 5 == 0:
                output.append('Buzz')
            else:
                output.append(str(i))
        return output


n = 15
s1 = Solution()
print(s1.fizzBuzz(n))