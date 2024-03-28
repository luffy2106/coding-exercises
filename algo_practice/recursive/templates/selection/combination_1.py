"""
I. Question
[Leet code]

https://leetcode.com/problems/combinations/description/

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:
    Input: n = 4, k = 2
    Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    Explanation: There are 4 choose 2 = 6 total combinations.
    Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:
    Input: n = 1, k = 1
    Output: [[1]]
    Explanation: There is 1 choose 1 = 1 total combination.
 
Constraints:

1 <= n <= 20
1 <= k <= n


II. Solution

Solution 1:
1. Base case :
If n = 0 , return empty list
2. Recursion case :
- Choose random number in the list, exclude it
- recursive looking for all the permutation of list of k elements from the remain list

Solution 2:


Note:
- permutation : A permutation is an arrangement of items in a specific order. selecting items "A, B, C" is different from selecting "C, B, A". 
when we want permutation, use list.
- combination : A combination is a selection of items without considering the order.  selecting items "A, B, C" is considered the same as selecting "C, B, A".
when we want permutation, use set.
"""

from typing import List
import copy
from itertools import combinations

class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        list_element =  list(range(1, n+1))
        current_combination = set()
        all_combinations = []
        return self.recursive_combine(list_element, k, current_combination, all_combinations)


    def recursive_combine(self, list_element: List[int], k: int, current_combination, all_combinations) -> List[List[int]]:
        # Define base case:
        if len(current_combination)==k:
            if current_combination not in all_combinations: 
                all_combinations.append(current_combination)
        else:
            # do recursive
            if len(list_element) > 0:
                for index in range(0, len(list_element)):
                    remain_list_element = [list_element[i] for i in range(0, len(list_element)) if i!=index]
                    temp_current_combination = copy.deepcopy(current_combination)
                    temp_current_combination.add(list_element[index])
                    self.recursive_combine(remain_list_element, k, temp_current_combination, all_combinations)
        
        all_combinations = [list(e) for e in all_combinations]
    
        return all_combinations


        


    

def main():
    # Write your main code logic here
    n = 4
    k = 2
    print("This is the main function.")
    x = Solution()
    list_element = list(range(1,n+1))
    print(x.combine(n,k))

    # using built-in function
    list_combination = [list(e) for e in list(combinations(list_element,k))]
    print(list_combination)

if __name__ == "__main__":
    main()

    
