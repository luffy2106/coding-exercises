# Monotonic stack

A monotonic stack is a special data structure used in algorithmic problem-solving. Monotonic Stack maintaining elements in either non-increasing or non-decreasing order. It is commonly used to solve problems where we need to find the next greater element, next smaller element, or nearest larger element for each element in an array(from the right, start from the index of the current considered number)



#### How it works

A Monotonic Stack is a common data structure in computer science that maintains its elements in a specific order. Unlike traditional stacks, Monotonic Stacks ensure that elements inside the stack are arranged in an increasing or decreasing order based on their arrival time. In order to achieve the monotonic stacks, we have to enforce the push and pop operation depending on whether we want a monotonic increasing stack or monotonic decreasing stack.

A stack is called a monotonic stack if all the elements starting from the bottom of the stack is either in increasing or in decreasing order.

Types of Monotonic Stack:
Monotonic Stacks can be broadly classified into two types:

1. Monotonic Increasing Stack

A Monotonically Increasing Stack is a stack where elements are placed in increasing order from the bottom to the top. Each new element added to the stack is greater than or equal to the one below it. If a new element is smaller, we remove elements from the top of the stack until we find one that is smaller or equal to the new element, or until the stack is empty. This ensures that the stack always stays in increasing order.

Example: 1, 3, 10, 15, 17

Complexity Analysis:
- Time Complexity: O(N), each element from the input array is pushed and popped from the stack exactly once. Therefore, even though there is a loop inside a loop, no element is processed more than twice.
- Auxiliary Space: O(N)

2. Monotonic Decreasing Stack

A Monotonically Decreasing Stack is a stack where elements are placed in decreasing order from the bottom to the top. Each new element added to the stack must be smaller than or equal to the one below it. If a new element is greater than top of stack then we remove elements from the top of the stack until we find one that is greater or equal to the new element, or until the stack is empty. This ensures that the stack always stays in decreasing order.

Example: 17, 14, 10, 5, 1

Complexity Analysis:
- Time Complexity: O(N), each element is processed only twice, once for the push operation and once for the pop operation.
- Auxiliary Space: O(N) 

3. Application
You will use motonic stack when you want to find the closestsmaller/greater number of each number in a list. For example :

If we have this list:
[1,2,3,4,3]
The list which include the closest greater number of each number of the above list is:
[2,3,4,-1,-1]
- 2 is greater than 1 and it's the closest to 1
- 3 is greater than 2 and it's the closest to 2
- 4 is greater than 3 and it's the closest to 3
- on the right of 4 there is no number greater than 4 => -1
- on the right of 3 there is no number greater than 3 => -1

Just remember :
- If you want to find next greater : Use monotonic_decreasing_stack(the bottom is the highest)
- If you want to find next smaller : Use monotonic_increasing_stack(the bottom is the lowest)


4. Practice 

To be master in monotonic stack, solve all the leet code problems in the following link(most of the exercises is quite similar):
```
https://leetcode.com/discuss/study-guide/2347639/A-comprehensive-guide-and-template-for-monotonic-stack-based-problems
```

#### Full reference 
```
https://www.geeksforgeeks.org/introduction-to-monotonic-stack-data-structure-and-algorithm-tutorials/
```


