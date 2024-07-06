"""
https://www.interviewbit.com/problems/row-wise-unique/


Explain the output:
first row [2, 1, 1, 0, 1, 2, 3, 0, 0, 0] :
- number of times student 1 contact is 2
- number of times student 2 contact is 1
...
- number of times student 10 contact is 0
arr2d : input matrix   
"""


import numpy as np



def countfreq_solution_1(arr2d):
    """    
    Solution :
    - Use a dictionary to store the occurence of number in each row
    """
    final_matrix = []
    shape = np.shape(arr2d) 
    rows = shape[0]
    cols = shape[1]
    for i in range(rows):
        dict_row = {}
        rows_i = [0] * cols
        for j in range(cols):
            if arr2d[i][j] in dict_row.keys():
                dict_row[arr2d[i][j]] += 1
            else:
                dict_row[arr2d[i][j]] = 1
        for key in dict_row.keys():
            rows_i[key-1] = dict_row[key]
        final_matrix.append(rows_i)
    return final_matrix


def countfreq_solution_2(arr2d):
    """    
    Solution :
    - Count number of appearance of each number is a row, use a list to count the appearance of value x at the index x - 1
    - concatinate all the list and output the result
    """
    shape = np.shape(arr2d) 
    rows = shape[0]
    cols = shape[1]
    list_rows_output = []
    for i in range(rows):
        rows_id_i = [0] * cols
        for j in range(cols):
            rows_id_i[arr2d[i][j] - 1] += 1
        list_rows_output.append(rows_id_i)
    # output_matrix = np.array(list_rows_output)
    print(list_rows_output)
                
    


N = int(input())
list_ans = []
for i in range(N):
    nb_rows = int(input())
    matrix = []
    for i in range(nb_rows):
        row_i = [int(x) for x in input().split()]
        matrix.append(row_i)
    ans_test_i = countfreq_solution_2(matrix) 
    list_ans.append(ans_test_i)
    
for ans in list_ans:
    print(ans)