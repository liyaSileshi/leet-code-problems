'''
You are given two sorted arrays, A and B, where A has a 
large enough buffer at the end to hold B. Write a method
to merge B into A in sorted order.
Time complexity: O(max(arr1, arr2)^2)
Space complexity: O(1)
'''

#sort arr2 into arr1
def sort_merge(arr1, arr2):
  #have a pointer at both arrays
  p_a, p_b = 0, 0
  while p_a < len(arr1) and p_b < len(arr2):
    if arr1[p_a] <= arr2[p_b]:
      p_a += 1
    else:
      arr1.insert(p_a, arr2[p_b])
      p_a += 1
      p_b += 1
  print(arr1)
  print(arr2)
sort_merge([2,4,6,7], [3,4,5])