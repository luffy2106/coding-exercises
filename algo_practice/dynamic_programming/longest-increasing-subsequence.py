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

Solution:
We will solve this exercises by 2 approaches Top Down memoization and Bottom up Tabulation. The main common steps is
- Set up 2D matrix with row and columns length = length(nums) + 1, all the element is -1 by default
- if i == 0 and j == 0 : A[i][j] = 0
- Go from top to bottom or from bottom to the top 

Solution :

Let L(i) be the length of the LIS ending at index i such that arr[i] is the last element of the LIS. Then, L(i) can be recursively written as: 
- L(i) = 1 + max(L(j) ) where 0 < j < i and arr[j] < arr[i]; or 
- L(i) = 1, if no such j exists.
Ex :
Consider arr[] = {3, 10, 2, 11}







"""