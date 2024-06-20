"""
Question:
https://leetcode.com/problems/minimum-path-sum/description/?envType=study-plan-v2&envId=top-interview-150

Solution:

Suppose that we have a matrix where each position in the matrix is the minimum sum of the path from top left to this position. We can see that:

dp[i][j] = min(list neighbor of dp[i][j]) + grid[i][j]


"""
from typing import List

class Solution:


    
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        matrix = [[float("inf") for _ in range(cols)] for _ in range(rows)]        
        if len(grid) == 1:
            return sum(grid[0])
        else:
            matrix[0][0] = grid[0][0]
            if len(grid[0]) > 1:
                matrix[0][1] = matrix[0][0] + grid[0][1]
            if len(grid) > 1:
                matrix[1][0] = matrix[0][0] + grid[1][0]
            for i in range(rows):
                for j in range(cols):
                    if i == 0 and j == 0:
                        continue
                    if i >= 1 and j >= 1:
                        matrix[i][j] = min(matrix[i][j-1], matrix[i-1][j]) + grid[i][j]
                    elif i == 0 and j >= 1:
                        matrix[i][j] = matrix[i][j-1] + grid[i][j]
                    elif j == 0 and i >= 1:
                        matrix[i][j] = matrix[i-1][j] + grid[i][j]
                    

        return matrix[rows-1][cols-1]
        