"""
https://leetcode.com/problems/search-insert-position/
"""

from typing import List






class Solution:
    def binary_search(self, nums, target, left, right):
        # If the target is less than all elements in the list
        if target < nums[0]:
            return 0
        # If the target is greater than all elements in the list
        elif target > nums[len(nums)-1]:
            return len(nums)
        else:
            if left <= right:
                mid = (left+right) // 2
                if nums[mid] == target:
                    return mid
                else:
                    if nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                    return self.binary_search(nums, target, left, right)
            else:
                if nums[left] > target :
                    return left
                else:
                    return left + 1    

    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        return self.binary_search(nums, target, left, right)
        





