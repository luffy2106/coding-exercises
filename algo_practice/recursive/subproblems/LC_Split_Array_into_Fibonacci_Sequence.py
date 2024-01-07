"""
1. Question
[Leet code]

https://leetcode.com/problems/split-array-into-fibonacci-sequence/description/

You are given a string of digits num, such as "123456579". We can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list f of non-negative integers such that:
- 0 <= f[i] < 231, (that is, each integer fits in a 32-bit signed integer type),
- f.length >= 3, and
- f[i] + f[i + 1] == f[i + 2] for all 0 <= i < f.length - 2.

Note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from num, or return [] if it cannot be done.

2. Analyze solution

This problem belong to the template "Subproblems"
2.1 Pseudo code provided by ChatGPT
function splitIntoFibonacci(num):
    function backtrack(sequence, index, currentNum, sumOfLastTwo):
        if index == len(num):
            return len(sequence) >= 3

        for i in range(index, len(num)):
            if num[index] == '0' and i > index:
                break

            newNum = int(num[index:i+1])

            if len(sequence) >= 2 and newNum > sumOfLastTwo:
                break

            if len(sequence) < 2 or newNum == sumOfLastTwo:
                sequence.append(newNum)
                if backtrack(sequence, i+1, newNum, currentNum + newNum):
                    return sequence

                sequence.pop()

        return []

    return backtrack([], 0, 0, 0)


# Test cases
print(splitIntoFibonacci("1101111"))  # Output: [11, 0, 11, 11]
print(splitIntoFibonacci("112358130"))  # Output: []
print(splitIntoFibonacci("0123"))  # Output: []

Still don't understand the logic behind
"""

def check_constraint(num: str):
    validate = True
    # Check condition 1 and 2
    if not 1<=len(num)<=200 or not num.isdigit() :
        validate = False
    else: 
        validate = True
    return validate
        



def splitIntoFibonacci(num: str):
    return


def main():
    print(splitIntoFibonacci(5))



if __name__ == "__main__":
    main()