"""
Question :

https://leetcode.com/problems/unique-paths-ii/?envType=study-plan-v2&envId=top-interview-150

Solution:
As we can see, we need a matrix DP such that, the element DP[i][j] is number of ways from top left to index[i,j]. And we know that:
- DP[i][j] = DP[i-1][j] + DP[i][j-1] if i < rows - 1 and j < cols - 1
           = DP[i-1][j] if i < rows - 1 and j =  cols - 1 
           = DP[i][j-1] if i = rows - 1 and j <  cols - 1 


"""



from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[rows-1][cols-1] == 1:
            return 0
        
        DP = [[0 for j in range(cols)] for i in range(rows)]

        DP[0][0] = 1
        # Fill the first column based on obstacles
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    continue
                if obstacleGrid[i][j] == 0:
                    if j == 0:
                        DP[i][j] = DP[i-1][j]
        # Fill the first row based on obstacles
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    continue
                if obstacleGrid[i][j] == 0:
                    if i == 0:
                        DP[i][j] = DP[i][j-1]



        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 0:
                    DP[i][j] = DP[i-1][j] + DP[i][j-1]

        return DP[rows-1][cols-1]






obstacleGrid = [[0,1],[0,0]]
x  = Solution()
x.uniquePathsWithObstacles(obstacleGrid)