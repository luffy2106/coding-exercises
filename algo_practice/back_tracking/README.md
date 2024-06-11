# Back Tracking

##### How Does a Backtracking Algorithm Work?
A backtracking algorithm works by recursively exploring all possible solutions to a problem. It starts by choosing an initial solution, and then it explores all possible extensions of that solution. If an extension leads to a solution, the algorithm returns that solution. If an extension does not lead to a solution, the algorithm backtracks to the previous solution and tries a different extension.

The following is a general outline of how a backtracking algorithm works:
- Choose an initial solution.
- Explore all possible extensions of the current solution.
- If an extension leads to a solution, return that solution.
- If an extension does not lead to a solution, backtrack to the previous solution and try a different extension.
- Repeat steps 2-4 until all possible solutions have been explored.

##### When to Use a Backtracking Algorithm?
Backtracking algorithms are best used to solve problems that have the following characteristics:
- There are multiple possible solutions to the problem.
- The problem can be broken down into smaller subproblems.
- The subproblems can be solved independently.

##### Applications of Backtracking Algorithm
Backtracking algorithms are used in a wide variety of applications, including:
- Solving puzzles (e.g., Sudoku, crossword puzzles)
- Finding the shortest path through a maze
- Scheduling problems
- Resource allocation problems
- Network optimization problems

Reference:
```
https://www.geeksforgeeks.org/backtracking-algorithms/
```


### Note about back tracking:
- Break recursive by return
- Do backtracking by do the inverse action that you did before calling recursive. For example: if you add before recursive, you need to remove after calling recursive. If you remove something before recursive, you need to add it later after calling recursive. Ex:
for word in wordSet:
    if self.check_words_difference(previousWord, word):                
        path_words.append(word)
        wordSet.remove(word)
        self.generate_path(word, endWord, wordSet, path_words, list_path)
        path_words.pop()
        wordSet.add(word)
- Pay attention to shallow copy when working with mutalble object like List, Set, Dictionary. Ex: When you modified any element in the list, the reference you used before that also change, one way of prevent weird result is using shallow copy(take a look at example word_ladder.py for more details)

