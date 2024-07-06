
"""
https://www.interviewbit.com/problems/duplicates-detection/

Hint : use np.unique()
https://numpy.org/doc/stable/reference/generated/numpy.unique.html
"""

import numpy as np


def dupldet(a):
    """
    Faster technique and take advantage of numpy function
    """
    b,indices = np.unique(a,return_index = True)
    new = np.ones(len(a),dtype=bool)
    new[indices] = False
    print(new)

def dupldet(a):
    value_unnique, indice_unique = np.unique(a, return_index=True)
    array_a = np.array(a)
    for i in range(len(array_a)):
        if i in indice_unique:
            array_a[i] = False
        else:
            array_a[i] = True
    # by default, the  array in numeric type [0,1,10 ..], so we need to convert to boolean type
    print(array_a.astype(bool))




test_case = [0, 0, 3, 0, 2, 4, 2, 2, 2, 2]
test_case = [9, 0, 11, 1, 7, 13, 12, 1, 7, 2, 8, 13, 12, 0, 13]
test_case = [9, 13, 4, 0, 1, 11, 12, 9, 13, 0, 13, 1, 10, 8, 9, 0, 10, 8, 6, 4]
print(dupldet(test_case))



            
        