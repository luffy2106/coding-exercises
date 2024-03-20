
"""
[Leet Code]
https://leetcode.com/problems/fibonacci-number/

This problem belong to the template "Subproblems"

Follow general steps.
1. Define base case

F(0) = 0, F(1) = 1

2. Define recurvie case.

F(n) = F(n - 1) + F(n - 2), for n > 1.

"""


def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)    
    
def main():
    print(fib(5))



if __name__ == "__main__":
    main()