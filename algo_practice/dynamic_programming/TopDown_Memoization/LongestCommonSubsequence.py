"""
Question:
https://leetcode.com/problems/longest-common-subsequence/


Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
- For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
- Input: text1 = "abcde", text2 = "ace" 
- Output: 3  
- Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
- Input: text1 = "abc", text2 = "abc"
- Output: 3
- Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
- Input: text1 = "abc", text2 = "def"
- Output: 0
- Explanation: There is no such common subsequence, so the result is 0.

Solution:
Suppose :
- m = len(text1)
- n = len(text2)

1. Create 2D matrix Array A with rows = m + 1 and cols = n + 1, all the value of the matrix is -1
2. We know that the result will be A[m][n], now we will use recursion from top to bottom to calculate the A[m][n]. Note that the 
main difference of normal recursion and dynamic programming in this case is we store the value which is already calculated to make sure it does not
calculate again(recursion is expensive 0(2^n)).(*)
"""



class Solution:
    def recursive_fill_matrix(self, A, m, n, text1, text2):
        if (m == 0 or n == 0):
            return 0
        if (A[m][n] != -1): #(*)This is to make sure that we don't recalculate, only consider the position which is not calcualated yet 
            return A[m][n] 

        if text1[m-1]==text2[n-1]: 
            A[m][n] = self.recursive_fill_matrix(A, m-1, n-1, text1, text2) + 1
            return A[m][n]
        
        A[m][n] = max(self.recursive_fill_matrix(A, m-1, n, text1, text2), self.recursive_fill_matrix(A, m, n-1, text1, text2))
        return A[m][n]
    
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        rows = m + 1
        cols = n + 1
        A = [[-1 for j in range(cols)] for i in range(rows)]
        result = self.recursive_fill_matrix(A, m,n,text1, text2)
        return result
    


