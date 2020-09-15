# Array Index & Element Equality
'''
Given a sorted array arr of distinct integers, 
write a function indexEqualsValueSearch that returns 
the lowest index i for which arr[i] == i. Return -1 if 
there is no such index. Analyze the time and space
 complexities of your solution and explain its correctness.
'''

'''
input: arr = [-8,0,2,5]
output: 2 # since arr[2] == 2

input: arr = [-1,0,3,6]
output: -1 # since no index in arr satisfies arr[i] == i.f
'''
def index_equals_value_search(arr):
  
  #arr = [-3,-2,-1,1,3,5]
    #mid = 2            
   # arr[mid] = -1
  index = float('inf')
  left= 0
  right= len(arr) - 1

  #while left < right
  while left <= right:
    mid = (left + right) // 2
    if mid == arr[mid]:
      if mid < index:
        index = mid
        right = mid - 1

    elif mid < arr[mid]:
      right = mid - 1
      
    else:
      left = mid + 1

  if index == float('inf'):
    return -1
  
  return index