#!/bin/python3


#
# Complete the 'findMinCost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY efficiency as parameter.
#

def findMinCost(efficiency):
    efficiency.sort()
    min_cost = pow(10,9) * pow(10,5)
    for x in efficiency:
        cost = 0
        remain_efficiency = [a for a in efficiency if a is not x]
        pairs_remain = [(remain_efficiency[i], remain_efficiency[i+1]) for i in range(0,len(remain_efficiency)-1,2)]
        for pair in pairs_remain:
            cost += abs(pair[0]-pair[1])
        if cost < min_cost:
            min_cost = cost 
    return min_cost





    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    efficiency_count = int(input().strip())

    efficiency = []

    for _ in range(efficiency_count):
        efficiency_item = int(input().strip())
        efficiency.append(efficiency_item)

    result = findMinCost(efficiency)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
