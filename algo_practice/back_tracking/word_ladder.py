"""
https://leetcode.com/problems/word-ladder/

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
- sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, 
or 0 if no such sequence exists.

Example 1:
- Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
- Output: 5
- Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:
- Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
- Output: 0
- Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

Note: 
1. Solving Word Ladder Problem with Backtracking

While backtracking is a valid approach for solving certain problems, it may not be the most efficient method for the Word Ladder problem. The main reason is that backtracking typically involves exploring all possible solutions, which can lead to an exponential increase in time complexity.

In the case of the Word Ladder problem, using backtracking to explore all possible transformations between two words can result in a large number of unnecessary computations. The BFS algorithm is more suitable for this problem as it guarantees finding the shortest transformation sequence in an optimal manner.

However, if you still want to explore the backtracking approach for educational purposes or other reasons, you can implement it by recursively generating all possible transformations from one word to another. Just keep in mind that the backtracking solution may not be the most efficient for this particular problem.

If you have any more questions or need further clarification, feel free to ask!

2. Pay attention to shallow copy
In (*), explanation of list_path.append(path_words[:]) in the Provided Code:
- In the code snippet you shared, the function generate_path is recursively finding all possible transformation paths from a 
start word to an end word using a given word list. The result list is used to store these transformation paths.
- When list_path.append(path) is used, it appends a reference to the path list to the result list. This means that if the path list is 
modified later (e.g., by popping elements), those modifications will also reflect in the lists already appended to result. 
This is because they are pointing to the same list object in memory.
- On the other hand, list_path.append(path_words[:]) creates a shallow copy of the path list using slicing (path_words[:]) and appends 
this copy to the result list. This ensures that each path appended to result is independent of any subsequent modifications to the path list.
You can use the following approach, it's the same:

temp_path_words = copy.deepcopy(path_words)
list_path.append(temp_path_words)

"""
from typing import List
import copy

class Solution:
    def check_words_difference(self, str_1, str_2):
        # Note that length of all words is the same:
        count_diff = 0
        for i in range(len(str_1)):
            if str_1[i] != str_2[i]:
                count_diff += 1
        if count_diff == 1:
            return True
        else: 
            return False
        

    def generate_path(self, previousWord: str, endWord: str, wordSet: set, path_words : List[str], list_path : List[list] ):
        # Break the recursive in backtracking = return 
        if previousWord == endWord :
            print(path_words)
            list_path.append(path_words[:]) #(*)
            return 
        # Run the recursive along with backtracking
        for word in wordSet:
            if self.check_words_difference(previousWord, word):                
                path_words.append(word)
                wordSet.remove(word)
                self.generate_path(word, endWord, wordSet, path_words, list_path)
                path_words.pop()
                wordSet.add(word)
        
                
                
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        path_words = []
        path_words.append(beginWord)
        list_path  = []
        wordSet = set(wordList)
        self.generate_path(beginWord, endWord, wordSet, path_words, list_path)    
        if list_path:
            list_length = [len(e) for e in list_path]
            min_length = min(list_length)
            return min_length
        else:
            return 0


beginWord = "a"
endWord = "c"
word_list = ["a","b","c"]
test_solution = Solution()

result = test_solution.ladderLength(beginWord, endWord, word_list)

print(result)
