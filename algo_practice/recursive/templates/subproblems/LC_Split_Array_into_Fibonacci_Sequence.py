"""
I. Question [Need to revise but not the priority because it's quite complicated]
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
The base case will end the recursive when it see that "".join(current_list) = original string

2. Define recurvie case.
- element_3 : last emelent of fibo in the current string
- element_2 : second last element of fibo in the current string
- element_1 : first last element of fibo list in the current string
- current_list : Fibo list at the time of recursive
- possible_list : list of possible fibo list could be made from the original string, return any Fibonacci-like sequence split from num, or return [] if it cannot be done.
- num : orginal string, to check when we end the recursion
- count_move: Take into consideration when the sliding window of 3 elements move, at the beginning it behave differently
- remain_except_element_3 the remain of the current string after we exclude the element 3
- element 3 : the third element of the sliding window such as : element_3 = element_1  + element_2. When the sliding window move, element 2 become element 3 of the recursion function
"""
import copy
from typing import List
class Solution:

    def check_element_does_not_start_with_zero(self, element):
        if element.startswith("0"):
            if len(element)== 1:
                return True
            else:
                return False
        # add constraints
        if int(element) > pow(2,31) or int(element) < 0:
            return False 

        return True



    def generate_list_fibo_for_each_last_3(self, remain_except_element_3, element_3, current_list, possible_list,num, count_move):
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
        list_element_2 = [remain_except_element_3[i:] for i in range(1, len(remain_except_element_3))]
        list_element_2 = [element_2 for element_2 in list_element_2 if int(element_2) <= int(element_3) and self.check_element_does_not_start_with_zero(element_2)]
        for element_2 in list_element_2:
            remain_except_element_2 = remain_except_element_3[0:-len(element_2)]
            list_element_1 = [remain_except_element_2[i:] for i in range(0, len(remain_except_element_2))]
            list_element_1 = [element_1 for element_1 in list_element_1 if self.check_element_does_not_start_with_zero(element_1)]

            # list_element_1 = [element_1 for element_1 in list_element_1 if int(element_1) + int(element_2) == int(element_3)]
            # if int(remain_except_element_2[i:]) + element_2 == element_3]
            for element_1 in list_element_1:
                if int(element_1) + int(element_2) == int(element_3):
                    if count_move == 0:
                        current_list.append(int(element_3))
                        current_list.append(int(element_2))
                        current_list.append(int(element_1))
                    else:
                        current_list.append(int(element_1))
                    current_str = ''.join([str(e) for e in current_list[::-1]])
                    if current_str == num:
                        possible_list.append(current_list[:])
                        return possible_list
                    element_3 = element_2
                    remain_except_element_3 = remain_except_element_3[0:-len(element_3)]
                    count_move+=1
                    possible_list = self.generate_list_fibo_for_each_last_3(remain_except_element_3, element_3, current_list, possible_list,num, count_move)
                    if count_move == 0 :
                        current_list.pop()
                        current_list.pop()
                        current_list.pop()
                    else:
                        current_list.pop()

                
        return possible_list

    def splitIntoFibonacci(self, num: str) -> List[int]:
        """loop all possible last elements in the Fibonacci list, looking for the generated Fibonacci list correspond to this element 
        Args:
            num (_type_): _description_

        Returns:
            _type_: _description_
        """
        # num string need to have at least 2 elements to qualified
        if len(num) <= 2 or len(num)>200:
            return []
        # the list of possible last element of fibonaci list. Ex : 112358130, the last element could be ['2358130', '358130', '58130', '8130', '130', '30', '0']
        list_last_elment = [num[i:] for i in range(2,len(num))]
        list_last_elment = [last_element for last_element in list_last_elment if self.check_element_does_not_start_with_zero(last_element)]
        possible_list = []
        for last_element in list_last_elment:
            remain_except_last_element = num[0:-len(last_element)]  # Ex : 112358130. list of possible remain except last element.  Ex : 112358130, the remain could be ['11', '112', '1123', '11235', '112358', '1123581', '11235813']
            # current_list=[int(last_element)]
            current_list = []
            possible_list = self.generate_list_fibo_for_each_last_3(remain_except_last_element, last_element, current_list, possible_list, num, count_move=0)


            if possible_list: # If possible_list is not None or list_fibo_last_3 is not empty
                fibonaci_list = possible_list[0] 
                return fibonaci_list[::-1]
        return []






def main():
    num = "0000"
    x = Solution()
    print(x.splitIntoFibonacci(num))


if __name__ == "__main__":
    main()


