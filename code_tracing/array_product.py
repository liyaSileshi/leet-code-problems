# Product of Array Except Self

# Given an array nums of n integers where n > 1,  
# return an array output such that output[i] is 
# equal to the product of all the elements of nums 
# except nums[i].

# Input:  [1,2,3,4]
# Output: [24,12,8,6]

# variable : value
#  nums    : [1, 2, 3, 4]
#  left    : [1, 1, 2, 6]
#  left_product : 6
#  i = 3
#  right   : [24, 12, 4, 1]
#  right_product : 24
#  i = 0
# output_arr: [21, 12, 8, 6]

def product_arr(nums):
    output_arr = []
    #left and right array that holds left product and right product
    left = [0]*len(nums)
    right = [0]*len(nums) # initialize right with 0 values
    
    #set to 1 because there's no number to left of our first item
    # or to right of our last item
    left[0] = 1
    right[-1] = 1

    left_product = 1
    for i in range(1, len(nums)):
        left_product *= nums[i-1]
        left[i] = left_product
    
    right_product = 1
    for i in reversed(range(len(nums) - 1)):
        right_product *= nums[i+1]
        right[i] = right_product
    # print(right)

    #merge the two arrays
    for i in range(len(nums)):
        output_arr.append(left[i] * right[i])

    return output_arr


    #NAIVE APPROACH
    # output_arr = []
    # pointer = 0
    # while pointer < len(array):
    #     product = 1
    #     for i in range(len(array)):
    #         #check if i and pointer are not pointing to similar value
    #         if i != pointer:
    #             product *= array[i]
    #     output_arr.append(product)
    #     pointer += 1

    # return output_arr



print(product_arr([1,2,3,4]))