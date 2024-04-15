"""
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
- Input: nums = [1,12,-5,-6,50,3], k = 4
- Output: 12.75000
- Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:
- Input: nums = [5], k = 1
- Output: 5.00000
 
Constraints:
- n == nums.length
- 1 <= k <= n <= 105
- -104 <= nums[i] <= 104
"""

from typing import List



class Solution_naive:
    """Time complexity: O(k*n) as it contains two nested loops.
    """
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        max_average_sum = -104 
        for i in range(n-k+1): # the last i will be n-k, so the last window is [pln[n-k], ...pln[n-1]]
            current_sum = 0
            for j in range(k):
                current_sum = current_sum + nums[i+j]
            current_average_sum = current_sum / k
            if current_average_sum > max_average_sum:
                max_average_sum = current_average_sum
        return max_average_sum
    

class Solution_sliding_window_technique:
    """Time Complexity: O(n), where n is the size of input array arr[].
       Auxiliary Space: O(1)
    """ 
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        max_average_sum = -104 
        # Step 1 : Calculate sum of first sliding window side k
        window_sum = sum(nums[:k])
        max_average_sum = window_sum/k
        for i in range(n-k): 
            window_sum = window_sum - nums[i] + nums[i+k]
            next_avarage_sum = window_sum / k
            max_average_sum = max(max_average_sum, next_avarage_sum)
        return max_average_sum





def main():
    nums = [1,12,-5,-6,50,3]
    k = 4
    solution_sliding_window = Solution_sliding_window_technique()
    max_average  = solution_sliding_window.findMaxAverage(nums, k)
    # MIN = -104 * len(nums) 
    # Add your code here
    print("max average is {}".format(max_average))

if __name__ == "__main__":
    main()
