"""
1. Question
The question taken from here

https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/


2. Solution

Solution 1: 
- use dictionary to store all the index of array from left to right
- use another array to store the value, loop from the original array, if the value first apprear, add to the new array
- modify the original array based on the new array

Time complexity : O(n)
Space complexity : O(n)


Solution 2:
Take a look at the function : removeDuplicates_two_pointer

- use dictionary to store all the index of array from left to right
- use another array to store the value, loop from the original array, if the value first apprear, add to the new array
- Use two pointer as follow: left pointer slide and if it see a element, add to a dictionary. right pointer slide and if it meet another value which in the index lower,
then update dictionary by this index. 

Time complexity : O(n/2)
Space complexity : O(m) which m is unique value in the list which store in the set

Solution 3:
Made by chatGPT
Take a look at the function : removeDuplicates_two_pointer_chatGPT
- left pointer will be used to keep the continious unique number and it's last index
- right pointer will be used to loop the whole original list

Time complexity : O(n)
Space complexity : O(1) (bacause we don't use another data structure to store elements)

"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        dict_index = {}
        new_array = []
        nb_remove = 0
        nb_unique = 0
        for i in range(n):
            if nums[i] not in dict_index.keys():
                dict_index[nums[i]] = i
                new_array.append(nums[i])
                nb_unique+=1
            else:
                nb_remove+=1
        for i in range(len(new_array)):
            nums[i] = new_array[i]
        return nb_unique
    def removeDuplicates_two_pointer(self, nums: List[int]) -> int:
        n = len(nums)
        set_value = set()
        left_array = []
        middle_array = []
        right_array = []
        new_array = []
        i = 0
        j = len(nums)-1
        if i==j:
            return len(nums)

        while i < j:
            if nums[i] == nums[j]:
                if nums[i] not in set_value:
                    left_array.append(nums[i])
                    set_value.add(nums[i])                    
            else:
                if nums[i] not in set_value:
                    left_array.append(nums[i])
                    set_value.add(nums[i]) 
                if nums[j] not in set_value:
                    right_array.append(nums[j])
                    set_value.add(nums[j])
            i+=1
            j-=1
            if i == j:
                if len(nums)%2 == 1:
                    middle = nums[int(len(nums)/2)]
                    if middle not in set_value:
                        middle_array.append(middle)
                    

        
        new_array = left_array + middle_array + right_array[::-1]
        for i in range(len(new_array)):
            nums[i] =  new_array[i]
        return len(new_array)

    def removeDuplicates_two_pointer_chatGPT(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        # nums.sort()  # Sort the array (optional but helps in removing duplicates easily)

        left = 0
        right = 1

        while right < n:
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
            right += 1

        return left + 1


    

def main():
    nums = [0,0,1,1,1,2,2,3,3,4]
    solution =  Solution()
    print('ha')
    print(solution.removeDuplicate_two_pointer(nums))
    print('haha')




if __name__ == "__main__":
    main()

