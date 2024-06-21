"""
Question :

https://leetcode.com/problems/unique-paths-ii/?envType=study-plan-v2&envId=top-interview-150

Solution:
We need to store the following information:
- The current path to move from top left to bottom right, if we can't go anywhere to meet the target, do backtracking
- A matrix visited to check if this path already visited
- nb_path from [i,j] to bottom down  = sum of nb path from its neighbor to bottom down. If the path already visit, skip 

"""



from typing import List
import copy
class Solution:
    def get_neighbor(self, i, j, obstacleGrid):
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        list_neighbors = []
        if i < rows - 1 and j < cols - 1:
            list_neighbors = [[i + 1, j], [i, j + 1]]
        if i == rows - 1 and j < cols - 1:
            list_neighbors = [[i, j + 1]]
        if j == cols - 1 and i < rows - 1:
            list_neighbors = [[i + 1, j]]
        list_neighbors = [neighbor for neighbor in list_neighbors if obstacleGrid[neighbor[0]][neighbor[1]] != 1]
        return list_neighbors
        

    def nb_steps_to_target_start_from_location(self, i,j, obstacleGrid, nb_path, visited,dict_nb_path):
        # print('heh')
        if [i,j] == [len(obstacleGrid)-1, len(obstacleGrid[0])-1]:
            nb_path += 1
            return nb_path
        else:
            list_neighbors = self.get_neighbor(i,j,obstacleGrid)
            for neighbor in list_neighbors:
                i = neighbor[0]
                j = neighbor[1]
                if visited[i][j] == False:
                    visited[i][j] = True
                    str_i_j = str(i)+str(j)
                    if str_i_j in dict_nb_path.keys():
                        nb_path = dict_nb_path[str_i_j]
                    else:
                        temp_dict_nb_path = copy.deepcopy(dict_nb_path)    
                        nb_path = self.nb_steps_to_target_start_from_location(i,j, obstacleGrid, nb_path, visited,temp_dict_nb_path)
                        dict_nb_path[str_i_j] = nb_path 
                    visited[i][j] = False
                    
        return nb_path

    
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[rows-1][cols-1] == 1:
            return 0

        visited = [[False for j in range(cols)] for i in range(rows)]
        # print(visited)
        nb_path = 0
        # visited = set()
        dict_nb_path = {}
        nb_path = self.nb_steps_to_target_start_from_location(0,0, obstacleGrid, nb_path, visited, dict_nb_path)
        return nb_path



obstacleGrid = [[0,1],[0,0]]
x  = Solution()
x.uniquePathsWithObstacles(obstacleGrid)