# Two pointer algorithm

Two pointers is really an easy and effective technique that is typically used for searching pairs in a sorted array.
Given a sorted array A (sorted in ascending order), having N integers, find if there exists any pair of elements (A[i], A[j]) such that their sum is equal to X.

Note:
It only work for sorted array

#### Solution

Now let’s see how the two-pointer technique works. We take two pointers, one representing the first element and other representing the last element of the array, and then we add the values kept at both the pointers. If their sum is smaller than X then we shift the left pointer to right or if their sum is greater than X then we shift the right pointer to left, in order to get closer to the sum. We keep moving the pointers until we get the sum as X. 

This technique alway work because you already have an array in ascending order.

#### Complexity 

1. Time Complexity: O(N)

The function uses a two-pointer approach where the left pointer (i) starts at the beginning of the array and the right pointer (j) starts at the end of the array.
In each iteration of the while loop, either i or j gets incremented/decremented based on the sum of the elements at these pointers compared to the target.
Since the array is sorted, the pointers move towards each other until they meet or find a pair that sums up to the target.
The time complexity of this function is O(N) because in the worst case scenario, both pointers traverse through the entire array once.

2. Space Complexity: O(1)

The function only uses a constant amount of extra space for variables n, i, and j.
The space complexity of this function is O(1) as it does not use any data structures whose space requirements depend on the input size