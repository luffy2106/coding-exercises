"""
Question:

https://leetcode.com/problems/house-robber/


Solution:
Let L[i] is the maximum money the robber have until the house i:
- L[i] = max(L[i-2] + nums[i], L[i-1])
- L[0] = nums[0]
- L[1] = max(nums[0],nums[1])
"""


from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        L = [0] * len(nums)
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            L[0] = nums[0]
            L[1] = max(nums[0], nums[1])
            for i in range(2, len(L)):
                L[i] = max(L[i-2] + nums[i], L[i-1])
        return max(L) 