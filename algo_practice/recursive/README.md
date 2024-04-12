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

Reference :

Review materials at this path to understand the general steps to solve permutation problem :

```
coding-exercises/algo_practice/recursive/Reference/recursion_part_3
```
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

#### 1. Back tracking
During the recursive process, we might want to keep the variable update until it converge to the base case. However, sometimes we want the variable come back to the previous state after calling the recursive(especially when you call recursive in the loop function). In this case, we need to use a technique named "back tracking", the main ideas is to store the state of the variable into a temporary variable before calling recursive and call it back after calling recursive. 

In python, when we store the variable in a a temporary variable, we need to consider "shallow copy" problem. For this reason, back tracking has different method for each type of variable. 

1. Immutable objects:

Case 1:
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

Case 2:
If you want to update string during the recursive, there are 2 ways
1. Update by using list:
```
def generate_string(n, current_str=[]):
    if n == 0:
        return ''.join(current_str)  # Join the list elements to form the final string
    
    current_str.append(str(n))  # Append the current number to the list
    
    return generate_string(n-1, current_str)  # Recursive call with updated list

# Call the recursive function to generate a string with numbers from n to 1
result = generate_string(5)

print(result)  # Output: "54321"
```
In this example:
- The generate_string function takes an integer n as input and a list current_str to store the string.
- If n is 0, it joins the elements of the current_str list and returns the final string.
- Otherwise, it appends the current number (n) to the current_str list and makes a recursive call with n-1.
By using a list (current_str) to accumulate the string data and joining the elements at the end, we avoid creating multiple string objects during recursion. This simple example demonstrates the concept of storing and updating a string in a recursive function efficiently.

2. Update by concatinate new string
```
def generate_string(n, current_str=""):
    if n == 0:
        return current_str
    
    current_str = current_str + str(n)  # Update the string by concatenation
    
    return generate_string(n-1, current_str)

result = generate_string(5)

print(result)  # Output: "54321"
```
In this case:
- Each time current_str is updated by concatenation, a new string object is created.
- This results in creating multiple string objects in memory during each recursive call.
- The new string object is then passed to the next recursive call, leading to additional memory overhead.
While this approach may work for small inputs, it is less efficient compared to using a list to accumulate the string data in a recursive function. The method of updating current_str by concatenation may cause performance issues when dealing with large strings or a high number of recursive calls due to the creation of multiple string objects.

###### Remember :
Update string during the recursive might have weird behavior when your recursive function has loop:
```
def traverse_graph(node, chain, fbs, dict_pbs, traversed_node, dict_pbs_allocation, suggestion):
    list_child_node = node.get_list_child()
    list_child_value = [node.value for node in list_child_node]
    list_child_dict = [child+": "+dict_pbs[child] for child in list_child_value]
    if list_child_dict:
        logging.info("list pbs consider is : {}".format(list_child_dict))
        list_pbs_allocation, explanation = get_response_from_list_pbs(chain, fbs, list_child_dict)
        for pbs_allocation in list_pbs_allocation:
            if ":" in pbs_allocation:
                key,value = [x.strip() for x in pbs_allocation.split(":")]
                if key not in dict_pbs_allocation.keys():
                    dict_pbs_allocation[key] = value
        logging.info(("corresponding dict pbs allocation : {}".format(dict_pbs_allocation)))
        
        suggestion = suggestion + explanation #(*)
        
        logging.info("The explaination for {} is : {}".format(list_child_dict,explanation))
        for child_node in list_child_node:
            if child_node not in traversed_node:
                traversed_node.append(child_node)
                traverse_graph(child_node, chain, fbs, dict_pbs, traversed_node, dict_pbs_allocation, suggestion)
    
    # End recursive
    
    return dict_pbs_allocation, suggestion
```

In the above example, the final "suggestion" variable will not store all the value accumumated in the recursive function because in the step(*) the new suggestion comeback to the previous state after the function loop to another element.

The best solution is using a list to store list of string, then merger in later when the recursion process end
```
def traverse_graph(node, chain, fbs, dict_pbs, traversed_node, dict_pbs_allocation, list_suggestion):
    list_child_node = node.get_list_child()
    list_child_value = [node.value for node in list_child_node]
    list_child_dict = [child+": "+dict_pbs[child] for child in list_child_value]
    if list_child_dict:
        logging.info("list pbs consider is : {}".format(list_child_dict))
        list_pbs_allocation, explanation = get_response_from_list_pbs(chain, fbs, list_child_dict)
        for pbs_allocation in list_pbs_allocation:
            if ":" in pbs_allocation:
                key,value = [x.strip() for x in pbs_allocation.split(":")]
                if key not in dict_pbs_allocation.keys():
                    dict_pbs_allocation[key] = value
        logging.info(("corresponding dict pbs allocation : {}".format(dict_pbs_allocation)))
        
        suggestion_current_pbs = "The explaination for {} is : ".format(list_child_dict) + explanation
        list_suggestion.append(suggestion_current_pbs)

        logging.info("The explaination for {} is : {}".format(list_child_dict,explanation))
        for child_node in list_child_node:
            if child_node not in traversed_node:
                traversed_node.append(child_node)
                traverse_graph(child_node, chain, fbs, dict_pbs, traversed_node, dict_pbs_allocation, list_suggestion)
    
    # End recursive
    all_suggestion = "\n".join(list_suggestion)
    
    return dict_pbs_allocation, all_suggestion
```




3. Mutable objects

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



#### 2. Using loop in the recursive

Depend on where you put the recursive, the behavior of the recursive function will be really different :
- When the recursive call is made inside the loop, it results in a different traversal order known as "in-order traversal".
- When the recursive call is made before the loop, it results in a different traversal order known as "pre-order traversal"(DFS manner).
- When the recursive call is made after the loop, it results in a different traversal order known as "post-order traversal"(BFS manner).

Take a look at folder loop_in_recursive to see the example along with more detailed explaination.


#### 3. Return in recursive function

Example Illustrating the Difference in Using "return" vs Not Using "return":
Let's consider a simple recursive function that calculates the factorial of a number. We will compare two versions of the function: one using return and the other without.

```
def calculate_factorial_with_return(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial_with_return(n - 1)

def calculate_factorial_without_return(n, result=1):
    if n == 0:
        return result
    else:
        calculate_factorial_without_return(n - 1, result * n)
```
- In the first function calculate_factorial_with_return, we use return to explicitly return the calculated factorial value at each step of the recursion. The return values are propagated back through the recursive calls and can be captured by the caller.
- In the second function calculate_factorial_without_return, we don't use return within the recursive call. Instead, we rely on modifying the result variable as the recursion progresses. However, since we don't return this modified result, the final calculated factorial is lost and not accessible outside the function.

```
# Using calculate_factorial_with_return
result_with_return = calculate_factorial_with_return(5)
print("Factorial with return:", result_with_return)  # Output: 120

# Using calculate_factorial_without_return
result_without_return = calculate_factorial_without_return(5)
print("Factorial without return:", result_without_return)  # Output: None (since result is not returned)
```

When you run the code snippet above, you will see that calculate_factorial_with_return correctly returns and calculates the factorial value, while calculate_factorial_without_return does not return the calculated factorial value.



### Good reference
```
https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1126/
```
