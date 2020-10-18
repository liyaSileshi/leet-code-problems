class Solution:
  def searchMatrix(self, matrix, target):
      """
      :type matrix: List[List[int]]
      :type target: int
      :rtype: bool
      """
      #O(nlogn)
      #loop through each row in matrix
      for row in matrix:
          if target == self.binarySearch(row, target):
              return True
          
      return False

  
  #do a binary search for each matrix
  def binarySearch(self, row, target):
      low = 0
      high = len(row) - 1
      
      while low <= high:
          mid = low + (high - low) // 2
          if row[mid] == target:
              return row[mid]
          elif row[mid] > target:
              high = mid - 1
          else:
              low = mid + 1
              
      #if target not found
      return float('inf')