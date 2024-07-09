"""
(not finished yet, this problem is hard, not the priority)
Because the problem ask us to return the least number of moves, so we need to find the shortest path => we need to use BFS 

curr = 1
[curr + 1, min(curr + 6, n2)] = [2, min(7,36)] = [2,7]

We need to determine the location of next jump in the matrix by variable next. For example, when next = 15, location = (3, 2). We need to think about the formular to convert next to location in the matrix


"""
from queue import Queue
class Solution:
    def map_next_to_location(self, board):
        """
        Map next to location
        return : cells(List) : each index in a cell is a tuple (row, col) which corresponding to the location of next location in the matrix
        """
        cells = [None] * (n**2 + 1)
        label = 1
        columns = list(range(0, n))
        for row in range(n - 1, -1, -1):
            for column in columns:
                cells[label] = (row, column)
                label += 1
            columns.reverse()
        return cells



    def snakesAndLadders(self, board: List[List[int]]) -> int:
        rows = n = len(board)
        cols = len(board[0])
        cells = self.map_next_to_location(board)
        visited = [[False for j in range(cols)] for i in range(rows)]
        queue_k = Queue()
        start = 1 
        queue_k.put(start)
        visited[rows-1][0] = True
        while not queue_k.empty():
            current = queue_k.get()
            for next in range(current+1, min(current+6, n**n)):
                next_location = cells[next]
                row_next, col_next = next_location
                destination = (board[row_next][col_next] if board[row_next][col_next] != -1 else next)  



        
        