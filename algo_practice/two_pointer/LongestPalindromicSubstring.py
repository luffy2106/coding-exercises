"""
1. Question

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
General Approach to Finding Palindromic Substrings in a String:
1. Iterate Through String:
- Start by iterating through the given string character by character.
2. Expand Around Center:
- For each character in the string, treat it as the center of a potential palindrome and expand outwards to check if the substring is a palindrome.
- There are two cases to consider:
* Palindromes with odd length: Expand around the current character to the left and right until the characters don't match.
* Palindromes with even length: Expand around the current character and its right neighbor to the left and right until the characters don't match.
3. Identify Palindromic Substrings:
- Keep track of all palindromic substrings found during the expansion process.
4. Return Palindromic Substrings:
- After iterating through the entire string, return the list of palindromic substrings found.
"""

class Solution:


    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left, right, max_length,longest_palindrome):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(s[left:right+1]) > max_length:
                    longest_palindrome = s[left:right+1]
                    max_length = len(longest_palindrome)
                left-=1
                right+=1
            return longest_palindrome, max_length 
        # palindromes = set()
        max_length = 0
        longest_palindrome = ""
        for i in range(len(s)):
            longest_palindrome, max_length = expand_around_center(i,i, max_length,longest_palindrome)
            longest_palindrome, max_length = expand_around_center(i,i+1,max_length,longest_palindrome)

        
        return longest_palindrome