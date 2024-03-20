"""
https://leetcode.com/problems/valid-palindrome/description/

This problem belong to the template "Subproblems"

Follow general steps.
1. Define base case

- if len(s) = 0 or len(s) = 1  : S is palindrome
- If the first and last characters of the string are not equal, it is not a palindrome.
2. Define recurvie case.

We can recursively check if the substring excluding the first and last characters is a palindrome.

"""

class Solution:
    """Class to solve the problem, remember that we alway need 'self' as a variable in a function inside class. Plus, when we call variable
    or function inside class, we need to use self.variable or self.function 

    Returns:
        _type_: _description_
    """
    already_preprocess = False
    def isPalindrome(self, s: str) -> bool:
        if self.already_preprocess == False:
            s = self.preprocessing(s)
            self.already_preprocess = True
        if len(s) == 0 or len(s)==1:
            return True
        elif len(s) == 2:
            if s[0] == s[-1]:
                return True
            else:
                return False
        else:
            return self.isPalindrome(s[1:-1])
    
    def preprocessing(self, text):
        """Return the final preprocessed text after removing non-alphanumeric characters

        Args:
            text (str): text

        Returns:
            str: new text
        """
        new_text = ""
        for char in text:
            if char.isalnum():
                new_text = new_text + char
        return new_text
    

def main():
    s = "race a car"
    solution = Solution()
    if solution.isPalindrome(s):
        print("valid palindrome")
    else:
        print("non valid palindrome")

if __name__ == "__main__":
    main()


