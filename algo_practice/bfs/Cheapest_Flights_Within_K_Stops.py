"""
(not finished yet)

https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""


from queue import Queue
class Solution:
    def build_graph(self, flights, graph):
        for flight in flights:
            graph[flight[0]].append(flight[1])
        return graph


    def find_min_cost_path(self, path,src,dst, route):
        if src == dst:
            return


    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        MAX = pow(100, 2)
        graph = [[] for i in range(MAX)]
        visited = [False] * MAX
        path = [-1] * MAX
        queue_k = Queue()
        queue_k.put(src)
        visited[src] = True
        while not queue_k.empty():
            current = queue_k.get()
            if current == dst:
                break
            for neighbor in graph[current]:
                if visited[neighbor] == False:
                    queue_k.put(neighbor)
                    path[neighbor] = current
        min_cost = self.find_min_cost_path(path,src, dst)
        return min_cost
        


        