"""
I. Question
[Leet code]

https://leetcode.com/problems/split-array-into-fibonacci-sequence/description/

You are given a string of digits num, such as "123456579". We can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list f of non-negative integers such that:
- 0 <= f[i] < 231, (that is, each integer fits in a 32-bit signed integer type),
- f.length >= 3, and
- f[i] + f[i + 1] == f[i + 2] for all 0 <= i < f.length - 2.

Note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from num, or return [] if it cannot be done.

II. Analyze solution

This problem belong to the template "subproblem"

Follow general steps.
From each last elment in the string, try to find out the fibonaci list by recursive looking for the 2 previous numbers in the remain string


1. Define base case
The base case will end the recursive when it see that last_1+last_2+last_3 = current string

2. Define recurvie case.
- last_3 : last emelent of fibo in the current string
- last_2 : second last element of fibo in the current string
- last_1 : first last element of fibo list in the current string
- current_list : Fibo list at the time of recursive
- count : number of character left in the recursive, start from n to 0 

"""
import copy

def generate_list_fibo_for_each_last_3(remain_except_last_3, last_3, current_list, possible_list):
    """For each last 3, recursively find the next other element last_1 and last_2 such as : last_3 = last_1 + last_2
    
    The base case will end the recursive when it see that last_1+last_2+last_3 = current string
    Args:
        remain_except_last_3 (_type_): _description_
        last_3 (_type_): _description_
        count_remain_num (_type_): _description_
        current_list (list, optional): _description_. Defaults to [].

    Returns:
        _type_: _description_
    """
    list_last_2 = [remain_except_last_3[-i:] for i in range(1,len(remain_except_last_3))]
    list_last_2 = [last_2 for last_2 in list_last_2 if int(last_2) <= int(last_3)]
    for last_2 in list_last_2:
        last_1 = str(int(last_3) - int(last_2))  
        remain_except_last_3_last_2 = remain_except_last_3[:-len(last_2)]
        if remain_except_last_3_last_2.endswith(last_1): 
            # last_2 is qualified to the fibo list 
            temp_current_list = copy.deepcopy(current_list)
            temp_current_list.append(int(last_2))
            if remain_except_last_3_last_2 == last_1:
                # break recursive
                current_list.append(int(last_2))
                current_list.append(int(last_1))
                possible_list.append(current_list)
                return None
            generate_list_fibo_for_each_last_3(remain_except_last_3_last_2, last_2, temp_current_list, possible_list)
            
    return possible_list

def find_fibonacci(num):
    """loop all possible last elements in the Fibonacci list, looking for the generated Fibonacci list correspond to this element 
    Args:
        num (_type_): _description_

    Returns:
        _type_: _description_
    """
    if num.startswith("0"):
        return []

    list_last_3 = [num[-i:] for i in range(1,len(num)-1)]
    for last_3 in list_last_3:
        remain_except_last_3 = num[0:-len(last_3)]
        if len(remain_except_last_3) >=2:
            list_fibo_last_3 =  generate_list_fibo_for_each_last_3(remain_except_last_3, last_3, current_list=[], possible_list = [])
            if list_fibo_last_3: # If list_fibo_last_3 is not None or list_fibo_last_3 is not empty
                fibo_last_3 = list_fibo_last_3[0] 
                fibo_last_3.reverse()
                fibo_last_3.append(int(last_3))
                return fibo_last_3
    return []






def main():
    num = "1101111"
    print(find_fibonacci(num))


if __name__ == "__main__":
    main()



# class Solution:
#     def splitIntoFibonacci(self, num: str) -> List[int]:
#         def backtrack(sequence, index, currentNum, sumOfLastTwo):
#             if index == len(num):
#                 return len(sequence) >= 3

#             for i in range(index, len(num)):
#                 # Check for leading zeros in currentNum
#                 if num[index] == '0' and i > index:
#                     break

#                 newNum = int(num[index:i+1])

#                 # Check if currentNum is greater than the sum of last two numbers
#                 if len(sequence) >= 2 and newNum > sumOfLastTwo:
#                     break

#                 if len(sequence) < 2 or newNum == sumOfLastTwo:
#                     sequence.append(newNum)
#                     if backtrack(sequence, i+1, newNum, currentNum + newNum):
#                         return sequence

#                     sequence.pop()

#             return []
#         return backtrack([], 0, 0, 0)    
    




# DFS implementation
# class Solution:
#     def splitIntoFibonacci(self, num: str) -> List[int]:
#         def is_fibonacci_like(sequence):
#             for i in range(2, len(sequence)):
#                 if sequence[i-2] + sequence[i-1] != sequence[i]:
#                     return False
#             return True

#         def dfs(index, sequence):
#             if index == len(num):
#                 if len(sequence) >= 3 and is_fibonacci_like(sequence):
#                     return sequence
#                 else:
#                     return []

#             for i in range(index+1, len(num)+1):
#                 if num[index] == '0' and i > index+1:  # Skip numbers with extra leading zeroes
#                     break
                
#                 current_num = int(num[index:i])
#                 if current_num > 2**31 - 1:  # Check if the number exceeds the limit
#                     break
                    
#                 if len(sequence) < 2 or sequence[-2] + sequence[-1] == current_num:
#                     result = dfs(i, sequence + [current_num])
#                     if result:
#                         return result
            
#             return []

#         return dfs(0, [])