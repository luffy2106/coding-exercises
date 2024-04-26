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
1. Create 2D matrix Array A with rows = len(text1) + 1 and cols = len(text2) + 1, all the value of the matrix is -1
2. For each row in the maxtrix, we loop to each columns with the main ideas is we want to keep the number of character overlap during the loop:
- if i=j=0 : A[i-][j-1] = 0
- for i in range(1, len(rows)):
    for j in range(1, len(cols)):
        if text[i] == text[j] : A[i][j] = A[i-1][j-1] + 1
        else: A[i][j] = max(A[i-1][j], A[i][j-1]) 
  return A[m][n] 
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1) +1
        cols = len(text2) +1
        A = [[0 for j in range(cols)] for i in range(rows)]
        print(A)
        A[0][0] = 0
        A[0][1] = 0
        A[1][0] = 0
        
        for i in range(1, rows):
            for j in range(1, cols):
                if text1[i-1] == text2[j-1]:
                    A[i][j] = A[i-1][j-1] + 1 # It can be understand that the number of common substring at point [i,j] = the number of common substring at point [i-1,j-1] + 1
                else:
                    A[i][j] = max(A[i-1][j], A[i][j-1])
        return A[rows-1][cols-1]



