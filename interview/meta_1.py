

"""
Questions : https://leetcode.com/problems/palindromic-substrings/
"""

test = "abc"
substring = [test[i:j] for i in range(0,len(test)) for j in range(i+1, len(test)+1)]

palindromic = []
for i in range(len(substring)):
    if substring[i][::-1] == substring[i]:
        palindromic.append(substring[i])

print(palindromic)