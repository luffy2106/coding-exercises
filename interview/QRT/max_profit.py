"""
Suppose that we have a list of n integers [1, -2, -3, 4, -2, 6], you choose m continuous element from this list(such as m < k),
find the max sum that you can have from this m number

Ex:

The max sum you have in above example is : 4 - 2 + 6 = 8, and we choose m = 3

1. First solution(greed search)

1.1 Implementation
- list all possible sublist made from m continuos elements
- Calculate sum of each sublist and choose the max one

Check the implementation in the function getMaxProfit_solution_1
1.2. Complexity
The complexity of the provided code can be analyzed as follows:

1. Generating Sublists:
   - The first loop runs from 1 to k (inclusive), creating sublists of length e for each value of e.
   - For each iteration of this loop, a sublist of length e is created by slicing the original list pnl.
   - The number of sublists generated for each value of e is roughly len(pnl) - e + 1 => O(len(pnl))  = O(n)
   - Since we iterate over all possible values of e from 1 to k, the total number of sublists generated is approximately sum(i) for i=1 to k, which is O(k*len(pnl)) = O(k*n)

2. Finding Maximum Sum:
   - After generating all sublists, another loop iterates through all_sublist to find the sublist with the maximum sum.
   - Within this loop, we calculate the sum of each sublist, which takes O(e) time (where e is the length of the sublist). Since e < k so it will be o(k)
   - As there are O(k*n) sublists in all_sublist, the total time complexity of finding the maximum sum is O(k^2 * n).

Therefore, the overall time complexity of the provided code is O(k^2 * len(pnl)), where k is the integer input and e is the average length of the sublists generated. 

It's important to note that the space complexity of this code is also significant, as it stores all sublists in the `all_sublist` list, which could potentially grow large depending on the size of the input list pnl and the value of k.



2. Second solution

Sliding window prolem, review the theory at 

https://www.geeksforgeeks.org/window-sliding-technique/

Check the solution at getMaxProfit_solution_sliding_window function

The complexity of this approach is O(k*n)

3. Third solution

We still can optimize the sliding window solution but it will be the work in the future

"""


from typing import List
from queue import Queue




def getMaxProfit_solution_1(pnl, k):
    all_sublist= []
    for e in range(1,k+1):
        sublist_e = [pnl[i:i+e] for i in range(len(pnl)-e + 1)]
        all_sublist.extend(sublist_e)
    max_sum = 0
    for sublist in all_sublist:
        sum_sublist = sum(sublist)
        if sum_sublist > max_sum:
            max_sum = sum_sublist
    return max_sum


def getMaxProfit_solution_sliding_window(pnl, K):


    n = len(pnl)
    max_sum_total = -104 * n
    for k in range(K):
        max_sum_K = -104 * K
        # Step 1 : Calculate sum of first sliding window side k
        sum_k = sum(pnl[:k])
        for i in range(n-k): 
            sum_k = sum_k + pnl[i+k] - pnl[i]
            max_sum_K = max(sum_k, max_sum_K)
        max_sum_total = max(max_sum_K, max_sum_total)
        
    return max_sum_total


def main():
    # Your main code logic goes here
    pnl  = [1, -2, -3, 4, -2, 6]
    k = 3
    max_sum = getMaxProfit_solution_sliding_window(pnl,k)
    print("max sum is {}".format(max_sum))
if __name__ == "__main__":
    main()
