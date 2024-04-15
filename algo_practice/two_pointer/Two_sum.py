"""
The problem is taken from here:

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/


Solution:
Now let’s see how the two-pointer technique works. We take two pointers, one representing the first element and other representing the last element of the array, and then we add the values kept at both the pointers. If their sum is smaller than X then we shift the left pointer to right or if their sum is greater than X then we shift the right pointer to left, in order to get closer to the sum. We keep moving the pointers until we get the sum as X. 

This technique alway work because you already have an array in ascending order.

"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i  = 0
        j  = len(numbers)-1
        while i < j:
            if numbers[i] + numbers[j] > target:
                j-=1
            elif numbers[i] + numbers[j] < target:
                i+=1
            else:
                return [i+1,j+1]
            


def main():
    numbers = [2,7,11,15]
    target = 9
    x =  Solution()
    print(x.twoSum(numbers, target))