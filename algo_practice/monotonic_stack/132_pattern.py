"""
Question [hard, need to revise when have time]:
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
Return true if there is a 132 pattern in nums, otherwise, return false.

Example 1:
- Input: nums = [1,2,3,4]
- Output: false
- Explanation: There is no 132 pattern in the sequence.
Example 2:
- Input: nums = [3,1,4,2]
- Output: true
- Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

https://leetcode.com/problems/132-pattern/description/


Solution:    
- Find previous greater element for each number a.
- Once the previous greater element x is found, check the previous minimum element for x
- If the previous minimum number is smaller than the number a, we know the pattern exists


My solution:
- For each element a in the original list, find the next greater element x
- After founding x, find the list of all the next smaller of x, we call it list_smaller_x
- if any element in list_smaller_x > a, then we found the pattern


"""
from typing import List

class Solution:

    def find_previous_greater(self, nums):
        # A list to store the index of next greater element
        result = [-1] * len(nums)
        # A monotonic decreasing stack to find next greater
        decreasing_stack = []
        for i in range(len(nums)-1, -1, -1):
            current_num = nums[i]
            while decreasing_stack and nums[decreasing_stack[-1]] < current_num:
                top_stack = decreasing_stack.pop()
                result[top_stack] = i
            decreasing_stack.append(i)

        return result
    
    def find_minimum_until_current(self, nums):
        """For each number in the list, find the minimum of each number until current number

        Args:
            nums (list): list of numbers

        Returns:
            list: list of element where each element is the minimum until this current number
        """
        
        min_so_far = float('inf')
        result = []
        for num in nums:
            min_so_far = min(min_so_far, num)
            result.append(min_so_far)

        return result


    def find132pattern(self, nums: List[int]) -> bool:
        min_until_currents = self.find_minimum_until_current(nums)
        list_index_previous_greater = self.find_previous_greater(nums)
        for i in range(len(list_index_previous_greater)-1, -1, -1):
            if list_index_previous_greater[i] == -1:
                continue
            index_previous_greater_i = list_index_previous_greater[i] 
            previous_greater_i = nums[index_previous_greater_i]
            if min_until_currents[index_previous_greater_i] < nums[i]:
                return True
        return False




    def find132pattern_kien(self, nums: List[int]) -> bool:
        """
        This solution has limit time error, mainly because of loop inside loop in (*)
        """
        # For each element a in the original list, find the list of next greater element x
        for i in range(len(nums)):
            stack_greater_i = []
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    stack_greater_i.append(nums[j])
            for index_greater_i in range(len(stack_greater_i)):
                # find the list of all the next smaller of x, we call it list_smaller_x (*)
                stack_smaller_greater_i = []
                for index_greater_j in range(index_greater_i+1, len(stack_greater_i)):
                    if stack_greater_i[index_greater_j] < stack_greater_i[index_greater_i]:
                        stack_smaller_greater_i.append(stack_greater_i[index_greater_j]) 
                for element in stack_smaller_greater_i:
                    if element > nums[i]:
                        return True
        return False
            

                           

        


        
        
# Driver program to test the function
# Driver program to test the function
nums = [-1,3,2,0]
solution_test = Solution()
print(solution_test.find132pattern(nums))

# -2,2,1  [0,2,4]
