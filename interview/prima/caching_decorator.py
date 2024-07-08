"""
Python: Cache Decorator
Several mathematical functions are implemented using tail recursion. They are inefficient and need optimization. One obvious optimization is to use caching.
Implement a decorator that handles the caching.
Few things to note.
- The decorator itself takes an argument, limits. This is a dictionary of {index: max_value}. 
- If the argument at an index is greater than the max_value, return a ValueError with the message specified in the template comments.
- A function can have one or two arguments, and the decorator should be able to handle that
- The factorial function takes an optional argument, mod.
- The cache should work generically across the three functions without interfering with one another.
- sys.setrecursionlimit(220) has been set to allow the usage of the cache to pass all tests.
- Do not modify the existing functions or change the recursion limit.
Functions already implemented are as follows. They are not to be edited. Only write the decorator cache:

@cache({0: 100})  # Example limit: n must not be greater than 100
def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

@cache({0: 100})  # Example limit: n must not be greater than 100
def factorial(n: int, mod: int = None) -> int:
    if n == 0 or n == 1:
        return 1
    result = n * factorial(n - 1)
    if mod:
        return result % mod
    return result

@cache({0: 100, 1: 100})  # Example limit: both x and y must not be greater than 100
def power(x: int, y: int) -> int:
    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        half_power = power(x, y // 2)
        if y % 2 == 0:
            return half_power * half_power
        else:
            return half_power * half_power * x

"""

from functools import wraps

def cache(limits):
    def decorator(func):
        cache_data = {}
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check if any argument access the limit
            for index, max_value in limits.items():
                if args[index] > max_value:
                    raise ValueError(f"Argument at index {index} is greater than maximum allowed value {max_value}")
            # Create a key based on both args and kwargs to uniquely identify each call, we need to convert dictionary kwargs to tuple to be able to form a key because it's immutable object
            # key = (args, frozenset(kwargs.items()))
            key = (args, tuple(kwargs.items()))
            if key in cache_data:
                return cache_data[key]
            else:
                result = func(*args, **kwargs)
                cache_data[key] = result
                return result
        return wrapper
    return decorator

@cache({0: 100})  # Example limit: n must not be greater than 100
def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

@cache({0: 100})  # Example limit: n must not be greater than 100
def factorial(n: int, mod: int = None) -> int:
    if n == 0 or n == 1:
        return 1
    result = n * factorial(n - 1)
    if mod:
        return result % mod
    return result

@cache({0: 100, 1: 100})  # Example limit: both x and y must not be greater than 100
def power(x: int, y: int) -> int:
    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        half_power = power(x, y // 2)
        if y % 2 == 0:
            return half_power * half_power
        else:
            return half_power * half_power * x
        





print(power(2,2))
print(power(101,2))