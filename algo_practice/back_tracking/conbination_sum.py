"""
https://leetcode.com/problems/combination-sum/description/ (need to do again and again)

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:
- Input: candidates = [2,3,6,7], target = 7
- Output: [[2,2,3],[7]]
- Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
- Input: candidates = [2,3,5], target = 8
- Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
- Input: candidates = [2], target = 1
- Output: []
"""


"""
Follow the below steps to implement the idea:
- Sort the array arr[] and remove all the duplicates from the arr[] then create a temporary vector r. to store every combination and a vector of vector res.
- Recursively follow:
  - If at any time sub-problem sum == 0 then add that array to the res (vector of vectors).
  - Run a while loop till the sum – arr[I] is not negative and i is less than arr.size().
    - Push arr[i] in r and recursively call for i and sum-arr[i] ,then increment i by 1.
    - pop r[i] from back and backtrack. 

"""
import copy
from typing import List

class Solution:
    def get_list_combination(self, candidates: List[int], target: int, index:int=0, current_combination: List[int] = [], listCombinations: List[List] = []) -> List[List[int]]:
        if target == 0:
            listCombinations.append(current_combination)
            return
        for i in range(index, len(candidates)):
            if target - candidates[i] >= 0:
                current_target = target - candidates[i]
                temp_combination = copy.deepcopy(current_combination)
                temp_combination.append(candidates[i])
                self.get_list_combination(candidates, current_target, i, temp_combination, listCombinations)
                
        return listCombinations

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sorted array and keep the value only
        candidates = sorted(list(set(candidates)))
        list_combination = self.get_list_combination(candidates, target, current_combination=[], listCombinations=[])

        return list_combination

        