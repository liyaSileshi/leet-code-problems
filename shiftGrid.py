'''
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
'''
class Solution:
    def shiftGrid(self, grid, k):
        '''Method 2: zigzag(pattern) method'''
        '''
            Time Complexity: O(n*m)
            Space Complexity: O(1) - we aren't creating any new data
        '''
        num_rows = len(grid)
        num_cols = len(grid[0])
        #save the last elt
        previous = grid[-1][-1]
        #loop over the grid
        for i in range(num_rows):
            for j in range(num_cols):
                temp = grid[i][j] #save the value before it's replaced
                grid[i][j] = previous
                previous = temp #new prev value to replace the next num
        return grid
