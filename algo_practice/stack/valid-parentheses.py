"""
We use stack to solve the problem, whenever we see the top of stack and the next char form a valid parentheses, we remove top stack and skip the character. If in the end, the stack is empty, then we can conclude the string is valid parentheses
- Time complexity : O(n) because we only loop the srting once
- Space complexity : O(1) because we create a dictionary to check parentheses

"""

class Solution:
    def isValid(self, s: str) -> bool:
        dict_char = {"{":"}", "(":")", "[":"]"}
        stack = []
        for c in s:
            if not stack:
                if c in dict_char.keys():
                    stack.append(c)
                else:
                    return False
            else:
                if dict_char[stack[-1]] == c:
                    stack.pop()
                else:
                    if c in dict_char.keys():
                        stack.append(c)
                    else:
                        return False

        return (len(stack) == 0)
        


        
                     
        
        