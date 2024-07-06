"""
Solution:

We can see that :
Rotate = Transpose + reverse

1. Complexity : 
Suppose M is number of cells in the matrix
- Transpose : We swap all the cells => Complexity is O(M)
- Reverse : We reverse all the rows => Complexity is O(M)

"""

class Solution:
    def transpose(self, matrix):
        """
        transpose maxtrix : convert row to column and column to row
        """
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 
        return

    def reverse(self, matrix):
        """
        reverse the matrix: reverse each row of the matrix
        """
        for i in range(len(matrix)):
            matrix[i].reverse()
        return
    
    
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reverse(matrix)
        

    