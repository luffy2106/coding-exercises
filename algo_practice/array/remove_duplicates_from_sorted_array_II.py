"""
Question (need to revisied again):

https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
- Input: nums = [1,1,1,2,2,3]
- Output: 5, nums = [1,1,2,2,3,_]
- Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:
- Input: nums = [0,0,1,1,1,1,2,3,3]
- Output: 7, nums = [0,0,1,1,2,3,3,_,_]
- Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Constraints:
- 1 <= nums.length <= 3 * 104
- -104 <= nums[i] <= 104
- nums is sorted in non-decreasing order.


Solution:
The problem is about remove all duplicated element which has the count > 2. The arrys is sorted => we can use 2 pointer approach here:
- left pointer to track the first occured element
- right pointer to track the current element
If we found left pointer is different with right pointer, it mean the number is different:
- If nb of occurence > 2, we delete the redundant elemments and update the left and right pointer
- If nb of occurence < 2, we update the left and right pointer
- We reset number of occurence to 0
"""

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left_pointer = right_pointer = 0
        count_occur = 0
        n = len(nums)
        while right_pointer < n:
            if nums[left_pointer] == nums[right_pointer]:
                count_occur+=1
                right_pointer+=1
            else:
                if count_occur > 2:
                    nb_delete = count_occur - 2
                    for i in range(1, nb_delete + 1):
                        nums.pop(right_pointer-i)
                        n-=1
                    left_pointer = right_pointer - nb_delete
                    right_pointer = left_pointer
                else:
                    left_pointer = right_pointer
                count_occur = 0

        if count_occur > 2:
            nb_delete = count_occur - 2
            for i in range(1, nb_delete + 1):
                nums.pop(right_pointer-i)
                n-=1
        return
    

nums = [1,1,1,2,2,3]
x = Solution()
x.removeDuplicates(nums)