"""
Implementing a decorator for caching (also known as memoization) is a common optimization technique. This can help improve the performance of tail-recursive functions by storing previously computed results. 

Question:
Implementing decorator function for calculate fibonaci and power recursively

https://leetcode.com/problems/fibonacci-number/description/

"""


from functools import wraps

class Solution:
    def cache(func):
        cache_data = {}
        @wraps(func)
        def wrapper(self, *args):
            if args in cache_data:
                return cache_data[args]
            else:
                result = func(self, *args)
                cache_data[args] = result
                return result
        return wrapper
    
    
    @cache
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
    @cache
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        return x * self.myPow(x, n-1) 

