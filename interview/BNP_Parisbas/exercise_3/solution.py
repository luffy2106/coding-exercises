

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



giải thuật:
-sort 2 list từ thap den cao, coi chung nhu 2 stacks 
-loop tưng đợt xử lý
-ở mỗi loop, tìm task lớn nhất cho mỗi processor mà nó có thể xử lý đc

Ex:
đợt thứ 1:
giao task 6 cho 7,
task 4 cho 4,
task 3 cho 4
xong đợt 1

đợt 2:
giao task 2 cho 7, 
task 1 cho 4 

"""


from copy import deepcopy
from collections import defaultdict

class PQEntry:
    def __init__(self,value):
        self.value = value
    def __lt__(self, other):
        return self.value > other.value


def getMinimumTime(processSize, capacity):
    """
    This solution is made by Kien
    """
    processSize.sort()
    sorted_capacity_with_indices = sorted(enumerate(capacity), key=lambda x : x[1])
    # print(sorted_capacity_with_indices)
    sorted_indices_capacity = [element[0] for element in sorted_capacity_with_indices]
    sorted_capacity = [element[1] for element in sorted_capacity_with_indices]
    # print(sorted_indices_capacity)


    sorted_indices_capacity_start = deepcopy(sorted_indices_capacity)
    sorted_capacity_start = deepcopy(sorted_capacity)
    dict_task = defaultdict(list)
    
    # print(processSize)
    # print(sorted_capacity)
    # We will use stack for the next step
    while len(processSize) > 0:
        current_process = processSize.pop()
        capacity =  sorted_capacity_start.pop()
        if capacity < current_process:
            return -1
        current_index_capacity = sorted_indices_capacity_start.pop()
        if not sorted_indices_capacity_start:
            sorted_indices_capacity_start = deepcopy(sorted_indices_capacity)
            sorted_capacity_start = deepcopy(sorted_capacity)
        dict_task[current_index_capacity].append(current_process)

    

    # Choose the longest value in the dict_task, it will be the represent for the total time 
    max_length = max(len(value) for value in dict_task.values())
    interval = max_length - 1
    total_time = max_length + interval
    return total_time


# def getMinimumTime(processSizes, numProcessors, capacity):
#     """
#     This solution is made by ClaudeAI and it's wro,ng
#     """

#     # If we don't have any processes, return 0
#     if not processSizes:
#         return 0
        
#     # Sort processes in descending order to try largest first
#     processSizes.sort(reverse=True)
    
#     # Check if any process is larger than max capacity
#     if processSizes[0] > max(capacity):
#         return -1
        
#     # Initialize completion times for each processor
#     processor_times = [0] * numProcessors
    
#     # Try to assign each process to the processor that will finish earliest
#     for size in processSizes:
#         # Find processor with minimum completion time that can handle this size
#         min_time = float('inf')
#         best_processor = -1
        
#         for i in range(numProcessors):
#             if capacity[i] >= size:  # Check if processor can handle this size
#                 if processor_times[i] < min_time:
#                     min_time = processor_times[i]
#                     best_processor = i
        
#         if best_processor == -1:  # No processor can handle this size
#             return -1
            
#         # Assign process to the chosen processor
#         # Add 1 second pause if this isn't the first process on this processor
#         if processor_times[best_processor] > 0:
#             processor_times[best_processor] += 1
#         processor_times[best_processor] += size
    
#     # Return the maximum completion time among all processors
#     return max(processor_times)


def main():
    processSize = [2,5,3]
    m = 3
    capacity = [6,2,4]
    print("The minimum time to handle all process is : {}".format(getMinimumTime(processSize, capacity)))

if __name__ == "__main__":
    main()