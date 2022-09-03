

"""
In this exercices we will try to implement combinations and combinations_with_replacement 

Question :
- https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true
- https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true


Note :

The difference between combinations and combinations_with_replacement is “combinations_with_replacement” 
means all the possible arrangements or subsets that allow an element to repeat in a subset

"""


from itertools import combinations, combinations_with_replacement
[text, number] = ['HACK', 2]



print("test combinations")
for i in range(1, int(number)+1):
    list_combinations = list(combinations(text, i))
    text_combinations = ["".join(sorted(e)) for e in list_combinations]
    text_combinations.sort()
    print(*text_combinations, sep = "\n")


print("test combinations_with_replacement")
for i in range(1, int(number)+1):
    list_combinations = list(combinations_with_replacement(text, i))
    text_combinations = ["".join(sorted(e)) for e in list_combinations]
    text_combinations.sort()
    print(*text_combinations, sep = "\n")




