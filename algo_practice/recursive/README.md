This folder is for practicing recursion problem, it was taken from leetcode, interview of different companies. There are few tips to work on recursion problem as well


### General steps

1.  Identify the base case 
Determine the simplest version of the problem that can be solved directly without further recursion. This serves as the stopping condition for the recursion.

2.  Define the recursive case

Break down the problem into smaller subproblems that are similar in nature to the original problem. Formulate the solution to the original problem in terms of the solutions to these subproblems.

3.  Call the function recursively

In the recursive case, call the function again with a smaller input, moving closer towards the base case. This allows the problem to be broken down into smaller and simpler subproblems.

4.  Combine the results
In the recursive case, combine the results obtained from the recursive calls to get the final result for the original problem.

5.  Return the result

Once the base case is reached, return the final result obtained from the recursive calls.

### Tips from random expert 

#### 6 templates for solving recursion problems
If you want to become good at solving recursion problems, learn these 6 templates: 

1. Iteration

Any problem that can be solved with loops can also be solved using recursion.

Sometimes recursion provides a more concise and elegant solution, even if less efficient.

Example:

- traversing a linked list in reverse order

2. Subproblems

This pattern focus on defining and solving a smaller version of a problem.

The standard strategy to do this is removing something from the input.

Examples:

- find if a string is a palindrome

- find all the ways to climb n stairs

3. Selection 

Some problems can be solved by:

• Finding all the combinations of some input elements 

• Selecting the combination matching a given condition

Example:

- find all the possible ways to interleave 2 strings

4. Ordering

This pattern is similar to Selection, but the order of how the elements are combined matters.

Such problems can be solved by:

• Finding all the permutations

• Filtering them

Example:

- find all the N-digit numbers whose digits sum up to a target number.

5. Divide & Conquer

This pattern focus on splitting the problem into multiple subproblems:

• each subproblem is solved separately
• the solutions are combined to get the result

Example:

- find all the ways to parenthesize an expression

6. Depth First Search

This pattern finds a path in a tree or graph:

• Start at a node
• Recursively visit each node's neighbor
• Avoid repeating cycles

Example:

- find the path with the greatest product in a matrix from the top left to the bottom right corner

Reference
```
https://x.com/Franc0Fernand0/status/1743912610406223896?s=20
```

