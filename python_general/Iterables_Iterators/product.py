# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product


def get_value_equation(list_e,M):
    return sum([e*e for e in list_e])%M


[K,M] = [int(x) for x in input().split()]

list_of_list = []
for i in range(K):
    list_i = [int(x) for x in input().split()][1:]
    list_of_list.append(list_i)

max = 0
product_list = list(product(*list_of_list))

# print(product_list)
for list_e in product_list:
    value = get_value_equation(list_e, M)
    if value >  max:
        max = value

print(max)
