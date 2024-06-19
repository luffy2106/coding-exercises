"""
Question:
https://leetcode.com/problems/word-break/?envType=study-plan-v2&envId=top-interview-150


Solution:
Suppose that we have a list of boolean value check_word_break = [False] * (n + 1), check_word_break will have n + 1 element because we need the first element is true as base case. 
check_word_break[i] is the boolean present if the string until character i_th that can be made from word in wordDict. We can see that:
for j in range(i):
    if dp[j] == True and dp[j:i] in wordDict => dp[i] = True
"""

from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        check_word_break = [False] * (n+1)
        check_word_break[0] = True # 
        for i in range(1,n+1):
            for j in range(i):
                if check_word_break[j] and s[j:i] in wordDict:
                    check_word_break[i] = True
                    break
        return check_word_break[n]        