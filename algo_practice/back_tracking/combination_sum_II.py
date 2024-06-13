"""

https://leetcode.com/problems/combination-sum-ii/description/

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

- Input: candidates = [10,1,2,7,6,1,5], target = 8
- Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:
- Input: candidates = [2,5,2,1,2], target = 5
- Output: 
[
[1,2,2],
[5]
]
 

Constraints:
- 1 <= candidates.length <= 100
- 1 <= candidates[i] <= 50
- 1 <= target <= 30

"""
from typing import List
import copy
class Solution:
    def generate_combination(self, remain_candidates, current_list_candidate, target, list_combination, list_combination_check):
        # We consider the case [1,2,3] and [3,2,1] is the same before adding any other elements, we will reduce time complexity a lot
        combination_check = [0] * 50
        for candidate in current_list_candidate:
            combination_check[candidate] += candidate
        if combination_check not in list_combination_check: 
            list_combination_check.append(combination_check)
            if sum(combination_check) > target:
                return
            elif sum(combination_check) == target:
                list_combination.append(current_list_candidate[:])
                return
            else:
                for i in range(len(remain_candidates)):
                    current_list_candidate.append(remain_candidates[i])
                    temp_delete_candidate_i = remain_candidates[i]
                    remain_candidates.pop(i)
                    self.generate_combination(remain_candidates, current_list_candidate, target, list_combination, list_combination_check)
                    remain_candidates.insert(i, temp_delete_candidate_i)
                    current_list_candidate.pop()    
        
        return list_combination
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        current_list_candidate = []
        list_combination = []
        list_combination_check = []
        list_combination = self.generate_combination(candidates, current_list_candidate, target, list_combination, list_combination_check)
        return list_combination

