"""
(Need to revise again and again)
Question:
https://www.geeksforgeeks.org/next-smaller-element/ (*)


Solution:
we use a stack to store the index of element which is smaller than the current considered element 
Make the loop:
- if the current number smaller than the number with the index of the top stack => add index of that number to stack(1)
- if the current number bigger than the number with the index of the top stack => pop the index from the stack 
until current number smaller than the number with the index of the top stack

For full solution and deeper understanding, take a look at (*):
"""


def get_next_smaller_element(arr):
    n = len(arr)
    stack_decreasing = [] # store the index of the current considered element, the top of the stack expected to be the index of the 
    result = [-1] * n # store the value on the right which is smaller than the current value, default is -1, meaning no value on the right smaller than the current value

    for i in range(n):
        next_val = arr[i]
        while stack_decreasing and arr[stack_decreasing[-1]] > next_val:
            top_stack = stack_decreasing.pop()
            result[top_stack] = next_val
        stack_decreasing.append(i)
 
    return result




# Driver program to test the function
arr = [4, 8, 2, 1, 6, 10, 5]
print(get_next_smaller_element(arr))