"""
Question:

https://leetcode.com/problems/unique-paths/description/

Solution:

Using Dynamic programming

"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        rows = m
        cols = n
        # Let matrix as each element in the matrix represent from number of ways from top left to the location [i,j]
        matrix = [[0 for j in range(cols)] for i in range(rows)]
        matrix[0][0] = 1

        # Fill the first column
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    continue
                if j == 0:
                    matrix[i][j] = matrix[i-1][j]


        # Fill the first row
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    matrix[i][j] = matrix[i][j-1]

        for i in range(1, rows):
            for j in range(1, cols):
                matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]

        return matrix[rows-1][cols-1]
        