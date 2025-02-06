from queue import Queue

def isPossible(a, b, c, d):
    def getNeighbors(current_a, current_b):
        """
        Get neighbors of the current node
        """
        neighbors = [(current_a + current_b, current_b), (current_a, current_a + current_b)]
        # Keep within bounds
        neighbors = [neighbor for neighbor in neighbors if 1 <= neighbor[0] <= 1000 and 1 <= neighbor[1] <= 1000]
        return neighbors

    visited = set()  # To track visited nodes
    stack = Queue()  # Using Queue for stack-like behavior
    stack.put((a, b))  # Start from the initial state

    while not stack.empty():
        # Get the most recently added element (stack-like behavior)
        current_a, current_b = stack.get()

        if (current_a, current_b) == (c, d):
            return "Yes"

        if (current_a, current_b) not in visited:
            visited.add((current_a, current_b))  # Mark as visited

            # Add neighbors to the stack (LIFO behavior)
            for neighbor in reversed(getNeighbors(current_a, current_b)):
                if neighbor not in visited:
                    stack.put(neighbor)

    return "No"  # If no path is found
