class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #find which row has 0s and put those row number in an array
        row = []
        #find which col has 0s and put those col numbers in an array
        col = []
        
        #loop through the matrix and keep track of col and row where zeros are
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)

        #nullify row
        for i in row:
            self.nullify_row(matrix, i)
        
        #nullify col
        for j in col:
            self.nullify_col(matrix, j)
            
            
    def nullify_row(self, matrix, i):
        for j in range(len(matrix[0])):
            print(matrix[i][j])
            matrix[i][j] = 0
            
    def nullify_col(self,matrix,j):
        for i in range(len(matrix)):
            matrix[i][j] = 0