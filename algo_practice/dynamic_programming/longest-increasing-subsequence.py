"""

Question:

https://leetcode.com/problems/longest-increasing-subsequence/description/

Given an integer array nums, return the length of the longest strictly increasing subsequence

Example 1:
- Input: nums = [10,9,2,5,3,7,101,18]
- Output: 4
- Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:
- Input: nums = [0,1,0,3,2,3]
- Output: 4
Example 3:
- Input: nums = [7,7,7,7,7,7,7]
- Output: 1
 
Constraints:
- 1 <= nums.length <= 2500
- -104 <= nums[i] <= 104



Solution :

Let L(i) be the length of the LIS(longest strictly increasing) ending at index i such that arr[i] is the last element of the LIS. Then, L(i) can be recursively written as: 
- L(i) = 1 + max(list(L(j)) ) where 0 < j < i and arr[j] < arr[i]; or 
- L(i) = 1, if no such j exists.
Ex :
Consider arr[] = {3, 10, 2, 11}
- L[4] = max([L[i]  for i in [0,1,2,3] if arr[i] < arr[4]) + 1 
- L[3] = max(L[1], L[2]) + 1 and 3 greater than 1,2
- L[2] = max(L[1],L[0]) + 1 and 2 greater than 1
- L[1] = max(L[0]) + 1 and 1 greater than 0

"""
from typing import List
class Solution:
    def lengthOfLIS_DP(self, n, dict_LIS, nums: List[int]) -> int:
        if n == 0:
            return 1
        elif n >= 1:
            list_LIS = []
            for i in range(n-1):
                LIS_i = 0
                if nums[i] < nums[n-1]:
                    if i in dict_LIS.keys():
                        LIS_i = dict_LIS[i]
                    else:
                        LIS_i = self.lengthOfLIS_DP(i, dict_LIS, nums)
                    list_LIS.append(LIS_i)      
            
            # lengthOfLIS_DP_
            return max(list_LIS) + 1


    
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dict_LIS = {}
        result = self.lengthOfLIS_DP(n, dict_LIS, nums)
        return result


nums = [10,9,2,5,3,7,101,18]
x = Solution()
print(x.lengthOfLIS(nums))