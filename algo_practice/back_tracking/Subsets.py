"""

https://leetcode.com/problems/subsets/description/

Question:

Given an integer array nums of unique elements, return all possible 
subsets(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
- Input: nums = [1,2,3]
- Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:
- Input: nums = [0]
- Output: [[],[0]]
 

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique.
"""
from typing import List
import copy
class Solution:
    def generate_subset(self, current_set, remain_set, list_set):
        for num in remain_set:
            current_set.add(num)
            if current_set not in list_set: # Remember that we do backtracking only when we add new element in the list_set
                print(current_set)
                shallowed_current_set = copy.deepcopy(current_set)
                list_set.append(shallowed_current_set)
                remain_set.remove(num)
                self.generate_subset(current_set, remain_set, list_set)
                remain_set.add(num)
            current_set.remove(num)
        return list_set

    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums_set = set(nums)
        list_set = []
        current_set = set()
        list_set.append([])
        list_set = self.generate_subset(current_set, nums_set, list_set)
        return list_set