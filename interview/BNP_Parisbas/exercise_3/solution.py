

"""
Test case :
- Test 1
processSize = [2,5,3]
m = 3
capacity = [6,2,4]
output = 1 sec
- Test 2
processSize = [2,5,8]
m = 3
capacity = [6,7,4]
output = -1 (no solution)
- Test 3
processSize = [1,2,3,4,6]
m = 3
capacity = [4,7,4]
output = 3 sec


"""

import heapq


class PQEntry:
    def __init__(self,value):
        self.value = value
    def __lt__(self, other):
        return self.value > other.value


def getMinimumTime(processSize, capacity):
    """
    Generate by ChatGPT(wrong)
    """
    
    # Sort processes in descending order (largest first)
    processSize.sort(reverse=True)

    # Create a min-heap for processor availability
    processor_heap = [(0, c) for c in capacity]  # (time_available, capacity)
    heapq.heapify(processor_heap)

    # Process each process
    for process in processSize:
        # Temporarily hold popped processors to find a suitable one
        temp = []
        assigned = False

        while processor_heap:
            time_available, proc_capacity = heapq.heappop(processor_heap)
            if proc_capacity >= process:
                # Assign the process to this processor
                new_time_available = time_available + 1
                heapq.heappush(processor_heap, (new_time_available, proc_capacity))
                assigned = True
                break
            else:
                temp.append((time_available, proc_capacity))

        # Push back all temporarily held processors
        for item in temp:
            heapq.heappush(processor_heap, item)

        # If no processor could handle this process
        if not assigned:
            return -1

    # Calculate the total time taken as the maximum availability time
    total_time = max(time for time, _ in processor_heap)
    return total_time



def main():
    processSize = [1,2,3,4,6]
    m = 3
    capacity = [4,7,4]
    print(getMinimumTime(processSize, capacity))

if __name__ == "__main__":
    main()