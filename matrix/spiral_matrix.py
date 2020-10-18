class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      if len(matrix) == 0:
          return []
      
      #create an output array
      output = []
      
        #init corners
      top = 0 
      bottom = len(matrix) - 1
      left = 0 #to include left most col
      right = len(matrix[0]) - 1 #to include right most col
      
        
      #keep track of entire length
      length = len(matrix) * len(matrix[0])
      
      
      #while there is still element to put in array
      while len(output) < length:
          #move top -> right
          for i in range(left, right+1):
              #check if our size is still less than output
              if len(output) < length:
                  output.append(matrix[top][i])
                  print(output)
          top += 1 #move top 1 down
          
          
          #move down
          for i in range(top, bottom+1):
              #check if our size is still less than output
              if len(output) < length:
                  output.append(matrix[i][right])
                  print(output)
          right -= 1
          
          #move left
          for i in range(right, left-1, -1):
              #check if our size is still less than output
              if len(output) < length:
                  output.append(matrix[bottom][i])
                  print(output) 
          bottom -= 1
          
          #move up
          for i in range(bottom, top-1, -1):
              #check if our size is still less than output
              if len(output) < length:
                  output.append(matrix[i][left])
                  print(output) 
          left += 1
          
      return output
