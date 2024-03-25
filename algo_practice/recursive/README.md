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


### General tricks

### 1. Back tracking
During the recursive process, we might want to keep the variable update until it converge to the base case. However, sometimes we want the variable come back to the previous state after calling the recursive(especially when you call recursive in the loop function). In this case, we need to use a technique named "back tracking", the main ideas is to store the state of the variable into a temporary variable before calling recursive and call it back after calling recursive. 

In python, when we store the variable in a a temporary variable, we need to consider "shallow copy" problem. For this reason, back tracking has different method for each type of variable. 

1. Immutable objects:

No problem with shallow copy: If the compound object contains only immutable objects (objects that cannot be modified after creation, like integers, strings, or tuples)

Ex :
```
def countdown(n):
    if n == 0:
        return
    else:
        print(n)
        temp = n  # Store the current value of n
        n -= 1
        countdown(n)  # Recursive call
        n = temp  # Revert n back to its previous value

countdown(5)

Result : 5 4 3 2 1
```

2. Mutable objects

Problem with shallow copy: If you have a compound object containing mutable objects (objects that can be modified after creation), a shallow copy of that object will create a new object, but it will still reference the same nested mutable objects. Therefore, changes to the nested mutable objects will be reflected in both the original and the shallow copy.

For this reason the solution for backt tracking is a bit different, take a look at the example of Gorgias_Machine_Learning_Engineer interview:

```
def generate_list_pairs(list_num, current_list_pairs, possible_list_pairs):
    if len(list_num) == 2:
        # Break our of recursive
        current_list_pairs.append(list_num)
        possible_list_pairs.append(current_list_pairs)
        return 
    else:
        # Do the recursive
        for i in range(len(list_num)):
            for j in range(len(list_num)):
                if j != i:
                    pairs = [list_num[i], list_num[j]]
                    list_remain = [list_num[x] for x in range(len(list_num)) if x!=i and x!=j]
                    temp = copy.deepcopy(current_list_pairs)
                    temp.append(pairs)
                    generate_list_pairs(list_remain, temp, possible_list_pairs)
```

As you can see, I use deepcopy to store the value of current_list_pairs, so after I call recursive function, the current_list_pairs come back to the previous state, but the variable possible_list_pairs doesn't follow the change of the variable current_list_pairs. 



### 2. Using loop in the recursive

Depend on where you put the recursive, the behavior of the recursive function will be really different :
- When the recursive call is made inside the loop, it results in a different traversal order known as "in-order traversal".
- When the recursive call is made before the loop, it results in a different traversal order known as "pre-order traversal"(DFS manner).
- When the recursive call is made after the loop, it results in a different traversal order known as "post-order traversal"(BFS manner).

Take a look at folder loop_in_recursive to see the example along with more detailed explaination.