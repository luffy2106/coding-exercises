
"""
https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
"""


from collections import Counter

X = int(input())
list_size = [x for x in input().split()]
dict_size = Counter(list_size)
N = int(input())
total = 0

for n in range(N):
    [shoe_n, price_n] = [x for x in input().split()]
    if shoe_n in dict_size.keys():
        if dict_size[shoe_n] > 0:
            total += int(price_n)
            dict_size[shoe_n] -=1
        
        
print(total)