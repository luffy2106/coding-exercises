"""
Give 2 sorted array, find all elements in list 1 but not list 2
"""

# list_A = [2,4]
# list_B = [1,2,3,4]

# list_A = [1,1,3,3]
# list_B = [2,4]

list_A = [1, 2, 3, 4, 5, 6]
list_B = [4, 5, 6, 7, 8]


output = []

index_A, index_B = 0, 0
while index_A < len(list_A):
    if index_B < len(list_B) and list_A[index_A] > list_B[index_B]:
        index_B+=1
    elif index_B < len(list_B) and list_A[index_A] == list_B[index_B]:
        index_A += 1
        index_B += 1
    else:
        output.append(list_A[index_A])
        index_A+=1
    

print(output)
