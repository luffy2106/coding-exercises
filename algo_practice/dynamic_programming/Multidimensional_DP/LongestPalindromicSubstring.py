"""
1. Question(not finished, need to revise)

https://leetcode.com/problems/longest-palindromic-substring/description/?envType=study-plan-v2&envId=top-interview-150

Given a string s, return the longest palindromic substring in s.

Example 1:
- Input: s = "babad"
- Output: "bab"
- Explanation: "aba" is also a valid answer.

Example 2:
- Input: s = "cbbd"
- Output: "bb"
 
Constraints:
- 1 <= s.length <= 1000
- s consist of only digits and English letters.

2. Solution
The main idea behind the approach is that if we know the status (i.e., palindrome or not) of the substring ranging [i, j], 
we can find the status of the substring ranging [i-1, j+1] by only matching the character str[i-1] and str[j+1].

Start the base case:
- At the beginning, all the elements in the matrix is False
- All the single character is palindrome => DP[i][i] = True 
- If character is adjacent => the substring made from it also palindrome => DP[i][i+1] = True if s[i] == s[i+1]

Fill the matrix by dynamic programming:
- If the substring from i to j is not a palindrome, then the substring from i-1 to j+1 will also not be a palindrome. 
Otherwise, it will be a palindrome only if str[i-1] and str[j+1] are the same.

Base on this fact, we can create a 2D table (say table[][] which stores status of substring str[i . . . j] ), 
and check for substrings with length from 1 to N. For each length find all the substrings starting from each character i and 
find if it is a palindrom or not using the above idea. The longest length for which a palindrome formed will be the required asnwer.



"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = rows = cols = len(s)
        DP = [[False for j in range(cols)] for i in range(rows)]
        max_length = 1
        longest_palind = ""

        # Start the base case
        # All the single character is palindrome => DP[i][i] = True 
        for i in range(rows):
            DP[i][i] = True
        # If character is adjacent => the substring made from it also palindrome => DP[i][i+1] = True if s[i] == s[i+1]
        for i in range(n-1):
            if s[i] == s[i+1]:
                DP[i][i+1] = True
        
        # Fill the matrix by dynamic programming
        for i in range(rows):
            for j in range(cols):
                if DP[i][j] == True: 
                    if i >= 1 and j+1 <= n-1:
                        if s[i-1] == s[j+1]:
                            DP[i-1][j+1] = True
                            if len(s[i-1:j+2]) > max_length:
                                longest_palind = s[i-1:j+2]
                                max_length = len(longest_palind)  

                    



        return longest_palind

                    
        