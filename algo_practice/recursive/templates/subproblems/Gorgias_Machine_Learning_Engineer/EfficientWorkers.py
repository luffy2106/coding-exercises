#!/bin/python3
import copy

#
# Complete the 'find_min_cost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY efficiency as parameter.
#

# def find_min_cost(efficiency):
#     efficiency.sort()
#     min_cost = pow(10,9) * pow(10,5)
#     for x in efficiency:
#         cost = 0
#         remain_efficiency = [a for a in efficiency if a is not x]
#         pairs_remain = [(remain_efficiency[i], remain_efficiency[i+1]) for i in range(0,len(remain_efficiency)-1,2)]
#         for pair in pairs_remain:
#             cost += abs(pair[0]-pair[1])
#         if cost < min_cost:
#             min_cost = cost 
#     return min_cost

"""
Analyze the problem :
Step 1 : 
- Take the number out and keep the remain list.
Step 2 : 
- In the remain list, generate all the possible pairs(need to consider index instead of value), 
we will do this recursively by a function called generate_list_pairs.


Take a look at the picture docs/algorithm_illustrate.jpg to illustrate algorithm. 

Pseudo code:

function generate_list_pairs(list_num, current_list_pairs, possible_list_pairs):
    if length of list_num is 2:
        append list_num to current_list_pairs
        append current_list_pairs to possible_list_pairs
        return
    else:
        for i from 0 to length of list_num:
            for j from 0 to length of list_num:
                if j is not equal to i:
                    pairs = [list_num[i], list_num[j]]
                    list_remain = create a new list with elements from list_num except list_num[i] and list_num[j]
                    temp = create a deep copy of current_list_pairs
                    append pairs to temp
                    recursively call generate_list_pairs with arguments (list_remain, temp, possible_list_pairs)

"""



def generate_list_pairs(list_num, current_list_pairs, possible_list_pairs):
    if len(list_num) == 0:
        # Break our of recursive
        # current_list_pairs.append(list_num)
        possible_list_pairs.append(current_list_pairs)
        return None
    else:
        # Do the recursive
        for i in range(len(list_num)):
            for j in range(len(list_num)):
                if j != i:
                    pairs = [list_num[i], list_num[j]]
                    list_remain = [list_num[x] for x in range(len(list_num)) if x!=i and x!=j]
                    temp = copy.deepcopy(current_list_pairs)
                    temp.append(pairs)
                    generate_list_pairs(list_remain, temp, possible_list_pairs)
                    

def min_cost_possible_list_pairs(possible_list_pairs, minimum_cost):
    for list_pairs in possible_list_pairs:
        cost = 0
        for pairs in list_pairs:
            cost = cost + abs(pairs[0]-pairs[1])
        if cost < minimum_cost:
            minimum_cost = cost    
    return minimum_cost



def find_min_cost(efficiency):
    
    list_minimum_cost = []
    for exclude_worker in efficiency:
        minimum_cost_case = pow(10,9) * pow(10,5) 
        include_workers = [worker for worker in efficiency if worker!=exclude_worker]
        current_list_pairs = []
        possible_list_pairs=[]
        generate_list_pairs(include_workers, current_list_pairs, possible_list_pairs)    
        minimum_cost_case = min_cost_possible_list_pairs(possible_list_pairs, minimum_cost_case)
        list_minimum_cost.append(minimum_cost_case)

    minimum_cost = min(list_minimum_cost)
    return minimum_cost



def main():
    efficiency = [4,2,8,1,9]
    result = find_min_cost(efficiency)

    print(f"the minimum possible cost is {result}")



    # Write your code here

if __name__ == '__main__':
    main()




