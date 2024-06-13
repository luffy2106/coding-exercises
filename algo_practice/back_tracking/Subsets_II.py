"""

https://leetcode.com/problems/subsets-ii/description/

Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
- Input: nums = [1,2,2]
- Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
- Input: nums = [0]
- Output: [[],[0]]
 
Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
"""
import copy
from typing import List
class Solution:
    
    def generate_subset(self, current_list, remain_nums, list_subset):
        # Remember that we do backtracking only when we add new element in the list_subset. Remember to check [1,2] and [2,1] is the same => we solve this problem by sort the list before adding
        temp_current_list = copy.deepcopy(current_list)
        temp_current_list.sort()
        if temp_current_list not in list_subset:
            list_subset.append(temp_current_list)
            for i in range(len(remain_nums)):
                current_list.append(remain_nums[i])
                print(current_list)
                temp_deleted_num_i = remain_nums[i] 
                remain_nums.pop(i)
                self.generate_subset(current_list, remain_nums, list_subset)
                remain_nums.insert(i,temp_deleted_num_i)
                current_list.pop()    
        return list_subset

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        list_set = []
        current_list = []
        # list_set.append([])
        list_set = self.generate_subset(current_list, nums, list_set)
        return list_set        