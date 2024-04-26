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

In the below code, we define a function called fibonacci that calculates the nth number in the Fibonacci sequence. We use a dictionary object called cache to store the results of the function calls. If the input parameter n is already present in the cache dictionary, we return the cached result. Otherwise, we compute the result using recursive calls to the fibonacci function and store it in the cache dictionary before returning it.
Memoization can be used to optimize the performance of many functions that have repeated and expensive computations. By caching the results of function calls, we can avoid unnecessary computations and speed up the execution of the function.

Remember:
Dynamic programming TopDown = Recursion + Memoization
"""

class Solution:
    def fib(self, n: int, dict_fib : dict) -> int:
        if n in dict_fib.keys():
            return dict_fib[n]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib_n =  self.fib(n-1, dict_fib) + self.fib(n-2,dict_fib)        
            dict_fib[n] = fib_n
            return fib_n
