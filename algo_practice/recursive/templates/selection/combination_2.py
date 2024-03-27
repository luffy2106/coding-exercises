
"""
Question : get all possible combination of string from a given string, take into account 


Solution:
- Get one elment from the string, use this element to combine with other elemment in the remain string




"""

s  = "abc"
list_s = [e for e in s]
remain = list_s
pick = ""

all =  set()
def recursive(pick, remain):
    if len(remain)==0:
        return
    else:
        for i in range(len(remain)):
            merge = pick + remain[i]
            if merge not in all:
                all.add(merge)
            next_remain = [remain[e] for e in range(len(remain)) if e!=i]
            recursive(merge, next_remain)

recursive(pick, remain)

print(all)