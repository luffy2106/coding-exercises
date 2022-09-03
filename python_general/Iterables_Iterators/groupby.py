"""
This exercices is to understand groupby and how to implement it using itertools.

Question:

https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true


Tutorial:

https://www.geeksforgeeks.org/itertools-groupby-in-python/

https://docs.python.org/2/library/itertools.html#itertools.groupby



"""

import itertools

input_str = "1222311"

input_char = [int(x) for x in input_str]

key_func = lambda x: x

list_output = []

for key, group in itertools.groupby(input_char, key_func):
    list_output.append((key, len(list(group))))

print(*list_output, sep = " ")