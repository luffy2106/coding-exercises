"""
(Need to revise again and again)
Question:

Given an array, print the Next Smaller Element (NSE) for every element. The NSE for an element x is the first smaller element on the right side of x in the array. 
Elements for which no smaller element exist (on the right side), consider NSE as -1. 

Ex :
Input: [4, 8, 5, 2, 25]
Output: [2, 5, 2, -1, -1]
Explanation:
The first element smaller than 4 having index > 0 is 2.
The first element smaller than 8 having index > 1 is 5.
The first element smaller than 5 having index > 2 is 2.
There are no elements smaller than 4 having index > 3.
There are no elements smaller than 4 having index > 4.



Solution:

The problem is about finding next smaller, so we will use monotonic_increasing_stack

We use 2 data structure in here 
- (1)An increasing stack to store the index of element which is smaller than the current considered element 
- (2)A list of number where the value in each index is the index of the number in the original list which is smaller than the current index and it's the closest one. Ex:  [4, 8, 5, 2, 25] => [3, 2, 0, -1, 1]
Make the loop:
- if the current number bigger than the number with the index of the top stack => add index of that number to stack(1)
- if the current number smaller than the number with the index of the top stack => pop the index from the stack then update at the index of the list (2) the current value
until current number smaller than the number with the index of the top stack 

For full solution and deeper understanding, take a look at (*):

Reference :

https://www.geeksforgeeks.org/next-smaller-element/ (*)

See the simlar example in final_price_with_special_discount_in_shop.py:

https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

"""


def get_next_smaller_element(arr):
    n = len(arr)
    stack_increasing = [] # store the index of the current considered element from the original list
    result = [-1] * n # store the value on the right which is smaller than the current value, default is -1, meaning no value on the right smaller than the current value

    for i in range(n):
        next_val = arr[i]
        while stack_increasing and arr[stack_increasing[-1]] > next_val: # As long as the top stack is bigger than the current consider element, we remove top stack and update the smaller value of top stack by the current consider element. In this way, the next smaller value of top stack can alway be tracked  
            top_stack = stack_increasing.pop()
            result[top_stack] = next_val
        stack_increasing.append(i)
 
    return result




# Driver program to test the function
arr = [4, 8, 2, 1, 6, 10, 5]
print(get_next_smaller_element(arr))