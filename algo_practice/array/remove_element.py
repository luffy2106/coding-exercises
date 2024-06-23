"""
Question :
https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150


Solution:
We loop from the end to the beginning, when ever we see the val,
- we swap the current element with the last index of the list and move the last index to the left

"""


from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index_last = len(nums) - 1
        nums_equal_val = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                nums[i] = nums[index_last]
                index_last = index_last - 1
                nums_equal_val += 1
        nums_diff_val = len(nums) - nums_equal_val
        return nums_diff_val