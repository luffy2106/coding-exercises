"""
I. Question
https://leetcode.com/problems/climbing-stairs/description/    

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

II. Solution
This problem belong to the template "Subproblems"

Follow general steps.
Let's suppose 
- f(n) is the number of distinct ways you can clim to the staircase n_th

1. Define base case
- if n = 0, return 0
- if n = 1, return 1
- if n = 2, return 2

2. Define recurvie case.
- f(n)  = max(f(n - 1) + 1,f(n - 2) + 2)
"""

class Solution: 
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 2
        else:
            return max(self.climbStairs(n-1) + 1, self.climbStairs(n-2) + 2)

def main():
    x  = Solution()
    print(x.climbStairs(3))



if __name__ == "__main__":
    main()

