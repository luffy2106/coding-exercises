import numpy as np
import math
from statistics import median, mean
import copy

"""
Provided by the platform
"""




arr = np.array([[1.2, None, 1.3], [None, None, 0.3]]).astype(np.float64)

arr_bis = np.array([[None, None, -1.2], [None, None, None], [None, 10.0, 1.0]]).astype(
    np.float64  # conver None value to Nan value
)

arr_ter = np.array([[None, 1.1, -32.0, 10.3], [2.2, None, None, 9.9]]).astype(
    np.float64
)


def impute_data(arr):
    # Your code goes here
    nb_rows = arr.shape[0]
    nb_cols = arr.shape[1]
    mean_row_i = np.NaN
    mean_col_j = np.NaN
    median_row_i = np.NaN
    median_col_j = np.NaN

    list_mean_row = []
    list_median_row = []
    list_mean_col = []
    list_median_col = []
    list_row = []
    list_col = []

    for i in range(nb_rows):
        row_i = copy.deepcopy(arr[i, :])   # remember that if you don't use deep copy, everytime an element in numpy array change, other elements which refer to this element also change(swallow copy)
        value_row_i = [x for x in row_i if not math.isnan(x)]
        mean_row_i = np.NaN if np.all(np.isnan(row_i)) else mean(value_row_i)
        median_row_i = np.NaN if np.all(np.isnan(row_i)) else median(value_row_i)
        list_row.append(row_i)
        list_mean_row.append(mean_row_i)
        list_median_row.append(median_row_i)
    for j in range(nb_cols):
        col_j = copy.deepcopy(arr[:, j])
        value_col_j = [x for x in col_j if not math.isnan(x)]
        mean_col_j = np.NaN if np.all(np.isnan(col_j)) else mean(value_col_j)
        median_col_j = np.NaN if np.all(np.isnan(col_j)) else median(value_col_j)
        list_col.append(col_j)
        list_mean_col.append(mean_col_j)
        list_median_col.append(median_col_j)
    for i in range(nb_rows):
        for j in range(nb_cols):
            if math.isnan(arr[i][j]):
                try:
                    if np.all(np.isnan(list_row[i])) and np.all(np.isnan(list_col[j])):
                        continue
                    elif list_mean_row[i] >= list_median_row[i]:
                        arr[i][j] = list_mean_row[i]
                    elif (
                        np.all(np.isnan(list_col[j]))
                        or list_mean_row[i] >= list_mean_col[j]
                    ):
                        arr[i][j] = list_mean_row[i]
                    elif (
                        np.all(np.isnan(list_row[i]))
                        or list_mean_col[j] >= list_mean_row[i]
                    ):
                        arr[i][j] = list_mean_col[j]
                    elif (
                        np.all(np.isnan(list_row[i]))
                        or list_median_col[j] >= list_median_row[i]
                    ):
                        arr[i][j] = list_median_col[j]
                except:
                    continue
    return arr

    # return 0


"""
Provided by the platform
"""

print(arr)  # Example input
print(impute_data(arr))
print()
print(arr_bis)  # Example input
print(impute_data(arr_bis))
print()
print(arr_ter)  # Example input
print(impute_data(arr_ter))
# Python code​​​​​​‌​​‌‌​‌‌‌​​​‌​‌​​‌‌​‌‌​‌​ below
# Use print("Debug messages...") to debug your solution.
