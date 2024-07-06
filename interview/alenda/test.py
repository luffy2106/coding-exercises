
"""
Write a function that given an array of integers, it return duplicates and the number of times it appears.

Example 1
[1,2,3,4,6,6,7,8,9,5,2,6,1,8] #=> {1:2, 2:2, 6:3, 8:2}"
"""


list_a = [1,2,3,4,6,6,7,8,9,5,2,6,1,8]

dict_a = {}
clean_dict = {}

for a in list_a:
    if a in dict_a.keys():
        dict_a[a] +=1
        clean_dict[a] = dict_a[a]
    else:
        dict_a[a] = 1


# for key in dict_a.keys():
#     if dict_a[key] > 1:
#         clean_dict[key] = dict_a[key]



print(clean_dict)



