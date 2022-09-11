"""
The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, 
but the only difference is that a defaultdict will have a default value if that key has not been set yet. 
If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, 
set it to what you want.

More detailed :
https://www.geeksforgeeks.org/defaultdict-in-python/

Question:
https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

"""

# # Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

"""
Function to return a default
values for keys that is not
present
"""
def def_value():
    return "-1"

[n, m] = [int(x) for x in input().split()]
d = defaultdict(def_value)


for i in range(n):
    char_i = input()
    if char_i in d.keys():
        d[char_i].append(str(i+1))
    else:
        d[char_i] = []
        d[char_i].append(str(i+1))
for j in range(m):
    char_j = input()
    if d[char_j] == "-1":
        print(d[char_j])
    else:
        print(" ".join(d[char_j]).strip())






