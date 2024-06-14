"""

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

1. Question

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
- Input: s = "abcabcbb"
- Output: 3
- Explanation: The answer is "abc", with the length of 3.
Example 2:
- Input: s = "bbbbb"
- Output: 1
- Explanation: The answer is "b", with the length of 1.
Example 3:
- Input: s = "pwwkew"
- Output: 3
- Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
Constraints:
- 0 <= s.length <= 5 * 104
- s consists of English letters, digits, symbols and spaces.


2. Solution
Have a list to store sliding window
- When we see a repeting character, we reset the sliding window by new sliding window which start from after the first index of the old character in sliding window to the current character. Ex : if str is 'dkvfk' and current sliding window is 'dkvf' => new sliding window is 'vfk'  
- otherwise, keep append new character
- Don't forget to add sliding window when finish the loop (in case it was not added during the loop)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        list_sliding_window = []
        sliding_window = []
        list_s = list(s)
        for c in list_s:
            if c not in sliding_window:
                sliding_window.append(c)
            else:
                list_sliding_window.append(sliding_window)
                first_index_c_wd = sliding_window.index(c)
                sliding_window = sliding_window[first_index_c_wd+1:]        
                sliding_window.append(c)

        list_sliding_window.append(sliding_window)
        length_sliding_windwon = [len(sliding_windwon) for sliding_windwon in list_sliding_window]
        longest_length = max(length_sliding_windwon)

        return longest_length