"""
Question:
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
- Input: n = 2
- Output: 2
- Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
- Input: n = 3
- Output: 3
- Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

Solution:
Suppose L[n] is the number of ways to reach step n_th, we can see that:
- L[n] = L[n-1] + L[n-2]
- Need a dictionary to store the result so we don't have to recalculate

"""

class Solution: 
    def climbStairs_DP(self, n: int,dict_climb:dict) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            if n in dict_climb.keys():
                return dict_climb[n]
            else:
                climbStairs_n = self.climbStairs_DP(n-1, dict_climb) + self.climbStairs_DP(n-2, dict_climb)
                dict_climb[n] = climbStairs_n
                return climbStairs_n   

        

    def climbStairs(self, n: int) -> int:
        dict_climb = {}
        return self.climbStairs_DP(n, dict_climb)
            

        