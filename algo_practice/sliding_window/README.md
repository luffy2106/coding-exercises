# Sliding windown technique

Sliding Window problems are problems in which a fixed or variable-size window is moved through a data structure, typically an array or string, to solve problems efficiently based on continuous subsets of elements. This technique is used when we need to find subarrays or substrings according to a given set of conditions.

Ex :
- finding subarrays with a specific sum 
- finding the longest substring with unique characters
- solving problems that require a fixed-size window to process elements efficiently.


### How to implement it 

How to use Sliding Window Technique?
There are basically two types of sliding window:

1. Fixed Size Sliding Window:
The general steps to solve these questions by following below steps:
- Find the size of the window required, say K.
- Compute the result for 1st window, i.e. include the first K elements of the data structure.
- Then use a loop to slide the window by 1 and keep computing the result window by window.

Check the following exercises:
- maximum_avarage_subarray_I_easy.py

2. Variable Size Sliding Window:
The general steps to solve these questions by following below steps:
- In this type of sliding window problem, we increase our right pointer one by one till our condition is true.
- At any step if our condition does not match, we shrink the size of our window by increasing left pointer.
- Again, when our condition satisfies, we start increasing the right pointer and follow step 1.
- We follow these steps until we reach to the end of the array.

### How to Identify Sliding Window Problems:
- These problems generally require Finding Maximum/Minimum Subarray, Substrings which satisfy some specific condition.
- The size of the subarray or substring ‘K’ will be given in some of the problems.

### Complexity
- These problems can easily be solved in O(N2) time complexity using nested loops, using sliding window we can solve these in O(n) Time Complexity.
- Required Time Complexity: O(N) or O(Nlog(N))
- Constraints: N <= 106 , If N is the size of the Array/String.



Reference:
```
https://www.geeksforgeeks.org/window-sliding-technique/
```