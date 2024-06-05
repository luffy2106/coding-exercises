
"""
1. Question
https://leetcode.com/problems/next-greater-element-ii/

2. Solution
The problem is about finding next greater, so we will use monotonic_decreasing_stack
"""





from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # A list to store the value where each element is the smaller and the closest number to the element in the original list, the default is the original list
        result = [-1] * len(nums)
        # A list which is double length the original list to search in cycle
        double_nums = nums + nums
        length_nums = len(nums)
        # decreasing stack to update the next greater element of the original list
        decreasing_stack = []

        for i in range(len(double_nums)):
            current_number = double_nums[i]
            mod_i = i % length_nums 
            while decreasing_stack and nums[decreasing_stack[-1]] < current_number:
                top_stack = decreasing_stack.pop()
                result[top_stack] = current_number
            decreasing_stack.append(mod_i)
        return result
        
# Driver program to test the function
nums = [1,2,3,4,3]
solution_test = Solution()
print(solution_test.nextGreaterElements(nums))