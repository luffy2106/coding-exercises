"""
Question (Similar to the exercise NextSmallerElement.py )

https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/


Solution:

The problem is about finding next smaller, so we will use monotonic_increasing_stack
"""
from typing import List

from copy import deepcopy

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # A list to store the value where each element is the smaller and the closest number to the element in the original list, the default is the original list
        result = deepcopy(prices)
        # An increasing stack to update the index of the closest smaller number of each element
        stack_increasing = []
        for i in range(len(prices)):
            current_price = prices[i]
            while stack_increasing and prices[stack_increasing[-1]] >= current_price:
                top_stack = stack_increasing.pop()
                discount = prices[top_stack] - current_price 
                result[top_stack] = discount
            stack_increasing.append(i)
        return result


# Driver program to test the function
prices = [8,4,6,2,3]
solution_test = Solution()
print(solution_test.finalPrices(prices))