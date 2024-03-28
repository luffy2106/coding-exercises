
"""
Question : get all possible permutation and combination of string from a given string, take into account 


Solution : 
Get one elment from the string, use this element to combine with other elemment in the remain string
- Base case: if the string is empty, then return None
- Recursive case: Take one random element from string, try to take the permutation from the remain string. 

"""
import copy

s  = "abc"
list_s = [e for e in s]
remain = list_s
pick = ""
all =  []

def get_permutation(pick, remain):
    if len(remain)==0:
        return
    else:
        for i in range(len(remain)):
            merge = pick + remain[i]
            if merge not in all:
                all.append(merge)
            next_remain = [remain[e] for e in range(len(remain)) if e!=i]
            get_permutation(merge, next_remain)

get_permutation(pick, remain)

print(all)



current_combination = set()
all_combination = []


def get_combination(list_s, current_combination:set, all_combination: list):
    if len(list_s) == 0:
        return None
    else:
        for index in range(0, len(list_s)):
            remain_list = [list_s[e] for e in range(0, len(list_s)) if e!=index]
            temp_current_combination = copy.deepcopy(current_combination)
            temp_current_combination.add(list_s[index])
            if temp_current_combination not in all_combination:
                all_combination.append(temp_current_combination)
            get_combination(remain_list, temp_current_combination, all_combination)
    
    all_combination = ["".join(list(e)) for e in all_combination]
    return all_combination


print(get_combination(list_s, current_combination, all_combination))



