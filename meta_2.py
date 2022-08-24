"""
https://leetcode.com/problems/max-area-of-island/
"""

"""
From one point, find path to go to all the near point
"""

from queue import Queue
import queue

class Position:
    """
    Position of element in matrix 2D
    """

    def __init__(self, row, column):
        self.row = row
        self.column = column

def valid_move(move_i, move_j, rows, columns):
    if 0 <= move_i <= rows-1 and 0 <= move_j <= columns-1:
        return True
    else:
        return False


def get_neighbors(position, queue_BFS, matrix, visited):
    rows = len(matrix)
    columns = len(matrix[0])
    for [i,j] in [[-1,0],[1,0],[0, 1], [0,-1]]:
        move_i = position.row + i
        move_j = position.column + j
        if (valid_move(move_i, move_j, rows, columns) and matrix[move_i][move_j] == 1 and visited[move_i][move_j] == False):
            neighbor = Position(move_i, move_j)
            queue_BFS.put(neighbor)
            visited[move_i][move_j] = True
    return queue_BFS


def BFS(s, visited, matrix):
    area = 0
    visited[s.row][s.column] = True
    queue_BFS = Queue()
    queue_BFS.put(s)
    while not queue_BFS.empty():
        u = queue_BFS.get()
        area+=1
        queue_BFS = get_neighbors(u,queue_BFS, matrix, visited)
    return area



class Solution:
    # def __init__(self, grid):
    #     self.grid =  grid

    def maxAreaOfIsland(self, grid):
        max_area = 0
        rows, columns = len(grid), len(grid[0])
        visited = [[False for j in range(columns)] for i in range(rows)]
        matrix = [[0 for j in range(columns)] for i in range(rows)]
        for i in range(len(grid)):
            row_i = grid[i]
            for j in range(len(row_i)):
                matrix[i][j] = row_i[j]
        
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 1 and visited[i][j] == False:
                    position_i_j = Position(i, j)
                    area_i_j = BFS(position_i_j, visited, matrix)
                    if area_i_j > max_area:
                        max_area = area_i_j
            
        return max_area


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

solution = Solution()

print(solution.maxAreaOfIsland(grid))