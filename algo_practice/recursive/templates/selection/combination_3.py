"""
Selecting the combination matching a given condition : Combination Sum

Question:

https://leetcode.com/problems/combination-sum/description/


Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Solution:

Check if the current list can sum up to target,the current list need to have all elements less than target

We need to use 2 time recursion:
- First recursion : From the input list, generate all possible list
- Second recursion : Check if this list can form the target or not by doing :
    Choose one elment from the current list, recursive check if the remain list can generate sum of : target - value of element took out

"""


import copy
from typing import List

class Solution:
    def list_qualified_combination(self, combination, target, current_combination = [], qualified_combinations=[]):
        if target <= 0:
            return
        if len(combination) == 1 :
            if target % combination[0] == 0:
                while target != 1:
                    target = int(target / combination[0])
                    current_combination.append(combination[0])
                if current_combination not in qualified_combinations:
                    qualified_combinations.append(current_combination)
        else:
            for i in range(len(combination)):
                remain_combination = [combination[j] for j in list(range(len(combination))) if i!=j]
                temp_current_combination = copy.deepcopy(current_combination)
                new_target = target - combination[i] # if you do target = target - combination[i], then the target will be changed forever, which is dan
                temp_current_combination.append(combination[i])
                self.list_qualified_combination(remain_combination, new_target, temp_current_combination, qualified_combinations)

        return qualified_combinations





    def list_combination(self, candidates: List[int], target: int, current_combination = set(), possbile_combination=[]) -> List[List[int]]:
        if len(candidates) == 0:
            if current_combination not in possbile_combination:
                possbile_combination.append(current_combination)
        else:
            for i in range(len(candidates)):
                remain_candidates = [candidates[j] for j in list(range(len(candidates))) if i!=j]
                temp_current_combination = copy.deepcopy(current_combination)
                temp_current_combination.add(candidates[i])
                if temp_current_combination not in possbile_combination:
                    possbile_combination.append(temp_current_combination)
                self.list_combination(remain_candidates, target, temp_current_combination, possbile_combination)
        possbile_combination = [list(e) for e in possbile_combination]
        return possbile_combination
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:    
        # print(candidates)
        possbile_combination = []
        list_combination =  self.list_combination(candidates, target, current_combination = set(), possbile_combination = [])
        for combination in list_combination:
            list_qualified_combination = self.list_qualified_combination(combination, target, current_combination=[], qualified_combinations=[])
            for qualified_combination in list_qualified_combination: 
                if qualified_combination:
                    possbile_combination.append(qualified_combination)
        
        return possbile_combination
    

def main():
    x = Solution()
    candidates = [2,3,6,7]
    target = 7
    # print(candidates)
    combination = [2,3]
    # print(x.list_qualified_combination(combination, target, current_combination = [], qualified_combinations=[]))
    print(x.combinationSum(candidates, target))

if __name__ == "__main__":
    main()