"""
https://leetcode.com/problems/max-area-of-island/

We will use DFS to solve this problem because we want to find all the possible case

"""

class Solution:
    def getNeighbors(self, i, j, grid):
        rows = len(grid)
        cols = len(grid[0])
        list_location_neighbors = [[i-1, j],[i, j-1], [i, j+1],[i+1, j]]
        list_location_neighbors = [neighbor for neighbor in list_location_neighbors if 0<=neighbor[0]<rows and 0<=neighbor[1]<cols]
        return list_location_neighbors
    
    def recursive_DFS(self,grid, i, j, connected_vertices, visited):
        visited[i][j] = True
        connected_vertices.append([i,j])
        list_neighbor = self.getNeighbors(i, j, grid)
        for neighbor in list_neighbor:
            if grid[neighbor[0]][neighbor[1]] == 1 and visited[neighbor[0]][neighbor[1]] == False:
                self.recursive_DFS(grid, neighbor[0], neighbor[1], connected_vertices, visited)
        return connected_vertices

    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for j in range(cols)] for i in range(rows)]
        list_connected_vertices = []
        for i in range(rows):
            for j in range(cols):
                if visited[i][j] == False and grid[i][j] == 1:
                    connected_vertices = []
                    connected_vertices = self.recursive_DFS(grid, i, j, connected_vertices, visited)
                    list_connected_vertices.append(connected_vertices)
        area_list = [len(connected_vertices) for connected_vertices in list_connected_vertices]
        max_area = 0
        for area in area_list:
            if area > max_area:
                max_area = area
        
        return max_area