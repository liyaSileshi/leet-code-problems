# def beerSong():
#     count = 99
#     while count > 0:
            
#             print(f'{count} bottles of beer on the wall, {count} bottles of beer')
#             print(f'You take one down, you pass it around {count-1} bottles of beer on the wall')
#             print('')
#             count -= 1


# beerSong()

# a1 = [0,1,5,7,20]
# a2= [2,3,4,10]

# # join = a1 + a2
# # print(join)

# for a in join:
#     # print(a)
#     print(


# """
# Intro:

# Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors. A factor is a number that evenly divides into another number, leaving no remainder. The simplest way to test if a one number is a factor of another is to use the modulo operation.

# The rules of raindrops are that if a given number:

# has 3 as a factor, add 'Pling' to the result.
# has 5 as a factor, add 'Plang' to the result.
# has 7 as a factor, add 'Plong' to the result.
# does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number.
# Examples
# 28 has 7 as a factor, but not 3 or 5, so the result would be "Plong".
# 30 has both 3 and 5 as factors, but not 7, so the result would be "PlingPlang".
# 34 is not factored by 3, 5, or 7, so the result would be "34".
# """
# num = int(input('enter a number: '))

# if num%5 == 0 and num%3 == 0:
#     print("pling plang")

# elif num%5 == 0 and num%7 == 0:
#     print('Plang plong')

# elif num%3 == 0 and num%7 == 0:
#     print('pling plong')

# elif num%3 == 0:
#     print('pling')

# elif num%5 == 0:
#     print('Plang')

# elif num%7 == 0:
#     print('Plong')

# else:
#     print(num)
    

# class Solution:
#     def reverseString(self, s):
#         """
#         Do not return anything, modify s in-place instead.
#         """

#         #change it to a string first
#         temp = ''.join(s)

#         #empty the original input
#         del s[:]
        
#         #reverse the string
#         temp = temp[::-1]

#         for ch in temp:
#             s.append(ch)

#         return s

# input=['h','e','l','l','o']
# s1= Solution()
# print(s1.reverseString(input))

class Monster:

    def __init__(self, name, catchphrase):
        self.name = name
        self.catchphrase = catchphrase

    def speak(self):
        return f"Hello my name is {self.name} and I say {self.catchphrase}"

monster_nova = Monster("nova", "roar")
print(monster_nova.speak())
#make lower case
print(monster_nova.speak().lower())