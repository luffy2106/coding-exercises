"""
Question :

https://leetcode.com/problems/daily-temperatures/description/


Solution:

The problem is about finding next greater, so we will use monotonic_decreasing_stack
"""




from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length_temp = len(temperatures)
        # the list include the number of days you have to wait after the ith day to get a warmer temperature. 
        result = [0] * length_temp
        # Since the problem is about finding next warmer temperature, we will use decreasing stack to update next warmer temperature
        decreasing_stack = []

        for i in range(length_temp):
            current_temperature = temperatures[i]
            while decreasing_stack and temperatures[decreasing_stack[-1]] < current_temperature:
                top_stack =  decreasing_stack.pop()
                days_wait = i - top_stack
                result[top_stack] = days_wait
            decreasing_stack.append(i)
        return result



# Driver program to test the function
temperatures = [73,74,75,71,69,72,76,73]
solution_test = Solution()
print(solution_test.dailyTemperatures(temperatures))
