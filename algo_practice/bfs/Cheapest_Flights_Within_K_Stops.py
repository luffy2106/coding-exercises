"""
(not finished yet)

https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""


from queue import Queue
class Solution:
    def build_graph(self, flights, graph):
        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))
        return graph



    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        MAX = pow(100, 2)
        graph = [[] for i in range(MAX)]
        visited = [False] * MAX
        dist = [0] * MAX
        path = [-1] * MAX
        queue_k = Queue()
        distance = min_cost = 0
        queue_k.put((src,distance))
        visited[src] = True
        dist[src] = 0
        while not queue_k.empty():
            (current_node, distance) = queue_k.get()
            for neighbor in graph[current_node]:
                (node_neighbor,price) = neighbor
                if price + distance < dist[node_neighbor]:
                    dist[node_neighbor] = price + distance
                    queue_k.put((node_neighbor,dist[node_neighbor]))
        return dist[dst]
        


        