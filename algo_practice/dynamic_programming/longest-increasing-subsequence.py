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
dp = [1] * n
Let dp[i] represents the length of the longest increasing subsequence ending with nums[i]
- dp[i] = max(dp[j] + 1, dp[i]) (in this way, the length of the longest increasing subsequen alway update in dp[i])

result = max(dp)



"""
from typing import List
class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # dp[i] represents the length of the longest increasing subsequence ending with nums[i]
        dp  = [1] * len(nums)  
        for i in range(1, len(dp)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)



nums = [10,9,2,5,3,7,101,18]
x = Solution()
print(x.lengthOfLIS(nums))