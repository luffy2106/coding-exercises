# Dynamic programming

Dynamic Programming is a method used in mathematics and computer science to solve complex problems by breaking them down into simpler subproblems. By solving each subproblem only once and storing the results, it avoids redundant computations, leading to more efficient solutions for a wide range of problems. This article provides a detailed exploration of dynamic programming concepts, illustrated with examples

More details:
Dynamic programming:
https://www.geeksforgeeks.org/dynamic-programming/

Top-Down Approach (Memoization)
https://www.geeksforgeeks.org/what-is-memoization-a-complete-tutorial/

The difference between Top-Down Approach (Memoization) and Top-Down Approach (Memoization)
https://www.geeksforgeeks.org/tabulation-vs-memoization/


#### Difference between Dynamic Programming and Recursive

Recursive:
- In recursive programming, a function calls itself in order to solve subproblems.
- It involves solving the same subproblems multiple times.
- It is simpler to implement and understand compared to dynamic programming.
- It may lead to exponential time complexity due to redundant calculations.
Dynamic Programming:
- Dynamic programming is a technique for solving complex problems by breaking them down into simpler subproblems.
- It involves storing the results of overlapping subproblems in a table (usually an array) to avoid redundant calculations.
- It typically has better time complexity compared to recursive solutions.
- It is more challenging to implement and requires careful design of the state transition and base cases.

In summary: 
- dynamic programming optimizes recursive algorithms by eliminating redundant calculations through storing and reusing intermediate results. 


#### How Does Dynamic Programming (DP) Work?
- Identify Subproblems: Divide the main problem into smaller, independent subproblems.
- Store Solutions: Solve each subproblem and store the solution in a table or array.
- Build Up Solutions: Use the stored solutions to build up the solution to the main problem.
- Avoid Redundancy: By storing solutions, DP ensures that each subproblem is solved only once, reducing computation time.

Dynamic programming can be achieved using two approaches:
1. Top-Down Approach (Memoization):
In the top-down approach, also known as memoization, we start with the final solution and recursively break it down into smaller subproblems. To avoid redundant calculations, we store the results of solved subproblems in a memoization table.

Let’s breakdown Top down approach:
- Starts with the final solution and recursively breaks it down into smaller subproblems.
- Stores the solutions to subproblems in a table to avoid redundant calculations.
- Suitable when the number of subproblems is large and many of them are reused.

2. Top-Down Approach (Memoization):
In the bottom-up approach, also known as tabulation, we start with the smallest subproblems and gradually build up to the final solution. We store the results of solved subproblems in a table to avoid redundant calculations.

Let’s breakdown Bottom-up approach:
- Starts with the smallest subproblems and gradually builds up to the final solution.
- Fills a table with solutions to subproblems in a bottom-up manner.
- Suitable when the number of subproblems is small and the optimal solution can be directly computed from the solutions to smaller subproblems.
