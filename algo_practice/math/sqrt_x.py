"""
Question:
https://leetcode.com/problems/sqrtx/?envType=study-plan-v2&envId=top-interview-150

"""

class Solution:
    def mySqrt(self, x: int) -> int:
        square = 0
        base = 0
        while True:
            square = base * base 
            if square > x:
                break
            base+=1   
        return base - 1
            