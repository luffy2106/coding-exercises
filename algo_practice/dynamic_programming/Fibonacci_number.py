"""
1. Question
https://leetcode.com/problems/fibonacci-number/description/


The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
- F(0) = 0, F(1) = 1
- F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
Example 1:
- Input: n = 2
- Output: 1
- Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:
- Input: n = 3
- Output: 2
- Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:
- Input: n = 4
- Output: 3
- Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

2. Complexity

If we use Recursion:
- Time Complexity : O(2^N). It can be calculated from the recurrence relation T(N) = T(N-1) + T(N-2). This is the most naive approach to calculate fibonacci number and recursion tree grows exponentially. There's a lot of repeated work that happens here
- Space Complexity : O(N), required for recursive call stack.
If we use Dynamic programming:
- Time Complexity : O(N), each fibonacci number is only calculated once.
- Space Complexity : O(N), required for memoization.


"""

class Solution:
    def fib(self, n: int) -> int:
        # Taking 1st two fibonacci numbers as 0 and 1
        f = [0, 1]
        for i in range(2,n+1):
            next_element = f[i-1] + f[i-2]
            f.append(next_element)
        return f[n]