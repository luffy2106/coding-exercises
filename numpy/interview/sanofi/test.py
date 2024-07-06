import numpy as np


"""
- change all the number 0 in each column by the mean of non-zero value in that column
- replace each number in each column by variance of that column
"""

import copy
import numpy as np

def solution(dataset):
    
    arr1 = np.array(dataset).astype(float)
    arr = copy.deepcopy(arr1)
    # print(arr.shape)
    sum_count_col = []
    for col in range(arr.shape[1]):
        count = 0
        for row in range(len(arr[:,col])):
            if arr[row][col] == 0:
               count+=1
        sum_count = len(arr[:,col]) - count
        sum_count_col.append(sum_count)
    # print(sum_count)
    for col in range(arr.shape[1]):
        for row in range(len(arr[:,col])):
            if arr[row][col] == 0:
                sum_col = np.sum(arr1[:,col])
                arr[row][col] = sum_col / sum_count_col[col]
    
    # print(arr)
    
    arr2 = copy.deepcopy(arr)
    
    for col in range(arr.shape[1]):
        # mean_col = np.sum(arr[:,col]) / sum_count_col[col]
        mean_col = np.mean(arr[:,col]) 
        std_col = np.std(arr[:,col])
        for row in range(len(arr[:,col])):
            arr2[row][col] = (arr[row][col] - mean_col)/std_col
            
    return arr2

dataset1 = [[1, 2, 0],
           [0, 1, 1],
           [5, 6, 5]]

dataset2 = [[1], 
 [7.3], 
 [0], 
 [5], 
 [13.5], 
 [22], 
 [9], 
 [0]]

print(solution(dataset1))