"""
Question:
https://leetcode.com/problems/triangle/?envType=study-plan-v2&envId=top-interview-150

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:
- Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
- Output: 11
- Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
- Input: triangle = [[-10]]
- Output: -10
 
Constraints:
- 1 <= triangle.length <= 200
- triangle[0].length == 1
- triangle[i].length == triangle[i - 1].length + 1
- -104 <= triangle[i][j] <= 104

Solution:
We call min_sum_until_row[i] is the minimum sum of path from top until row i. We have
- min_sum_until_row[i] = min_sum_until_row[i-1] + min(triangle[i])
- min_sum_until_row[0] = min(triangle[i])

We need to find min_sum_until_row[n], with n is the number of rows in the triangle

Solution 2:

We need to store 2 things: The current row(i) and the index of the current row(j) where the path to the current row is minimum, so we need 2D matrix


"""
"""
Question:
https://leetcode.com/problems/triangle/?envType=study-plan-v2&envId=top-interview-150

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:
- Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
- Output: 11
- Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
- Input: triangle = [[-10]]
- Output: -10
 
Constraints:
- 1 <= triangle.length <= 200
- triangle[0].length == 1
- triangle[i].length == triangle[i - 1].length + 1
- -104 <= triangle[i][j] <= 104

Solution:
We call min_sum_until_row[i] is the minimum sum of path from top until row i. We have
- min_sum_until_row[i] = min_sum_until_row[i-1] + min(triangle[i])
- min_sum_until_row[0] = min(triangle[i])

We need to find min_sum_until_row[n], with n is the number of rows in the triangle

Solution 2:
Check goodnote in ipad for the illustration

We need to store 2 things: The current row(i) and the index of the current row(j) where the path to the current row is minimum, so we need 2D matrix such as:
- Matrix[i][j] will store the minimim sum from the path from the top triangle to the position(i,j)
- If you draft the matrix, you will see:

matrix[i][j] =  min(matrix[i-1][j-1], matrix[i-1][j]) + triangle[i][j] if if len(triangle[i]) > j > 0
             =  matrix[i-1][j] + triangle[i][j] if j == 0

matrix[0][0] = triangle[0][0]  (top of the triangle) 
"""
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = rows = len(triangle)
        cols = len(triangle[-1])
        matrix = [[float("inf") for _ in range(cols)] for _ in range(rows)]
        if n == 1:
            return triangle[0][0]
        else:
            matrix[0][0] = triangle[0][0]
            for i in range(1, rows):
                for j in range(0, cols):
                    if len(triangle[i]) > j > 0:
                        print("i = {} and j = {}".format(i,j))
                        matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j]) + triangle[i][j]
                    elif j == 0:
                        matrix[i][j] = matrix[i-1][j] + triangle[i][j]
            return min(matrix[n-1])
            




            



