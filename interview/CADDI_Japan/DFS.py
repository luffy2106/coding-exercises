import sys
sys.setrecursionlimit(2000)  # Set a higher recursion limit

def isPossible(a, b, c, d):
    def getNeighbors(current_a, current_b):
        """
        Get neighbors of the current node
        """
        neighbors = [(current_a + current_b, current_b), (current_a, current_a + current_b)]
        neighbors = [neighbor for neighbor in neighbors if 1 <= neighbor[0] <= 1000 and 1 <= neighbor[1] <= 1000]
        return neighbors

    visited = set()
    is_possible = "No"

    def searchDFS(a, b):
        nonlocal is_possible
        if (a, b) == (c, d):
            is_possible = "Yes"
            return True

        visited.add((a, b))
        for neighbor in getNeighbors(a, b):
            if neighbor not in visited:
                if searchDFS(neighbor[0], neighbor[1]):
                    return True
        
        return False

    searchDFS(a, b)
    return is_possible
