# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
Question :

https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true

Tutorial about filter and other iterators technique:

https://docs.python.org/2/library/itertools.html

"""


import itertools

N = int(input())
list_char = [c for c in input().split()]
K = int(input())

list_combinations = list(itertools.combinations(list_char, K))
count = 0

list_contain_a = list(filter(lambda x: "a" in x, list_combinations))

print(round(len(list_contain_a)/len(list_combinations),3))