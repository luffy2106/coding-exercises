"""

1. Question
[need to revise many times]
https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/

You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:
- The length of the subarray is k, and
- All the elements of the subarray are distinct.

Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
Example 2:
Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.

We return 0 because no subarrays meet the conditions.

2. Solution

https://www.geeksforgeeks.org/maximum-sum-of-subarrays-having-distinct-elements-of-length-k/

"""



from typing import List

class Solution:
    def check_condition(self,dict_sliding_window, k):
        if len(dict_sliding_window.keys()) == k:
            return True 
        else:
            return False
    def update_dict_sliding_window(self, dict_sliding_window, num_delete, num_add):
        if num_delete in dict_sliding_window.keys():
            if dict_sliding_window[num_delete] > 1:
                dict_sliding_window[num_delete] -= 1
            else:
                dict_sliding_window.pop(num_delete)
        
        if num_add in dict_sliding_window.keys():
            dict_sliding_window[num_add] += 1
        else:
            dict_sliding_window[num_add] = 1
        return


    def maximumSubarraySum_Kien(self, nums: List[int], k: int) -> int:
        """This solution is made by me, it has the complexity of O(n) but still can not pass the unit test of leetcode

        Args:
            nums (List[int]): _description_
            k (int): _description_

        Returns:
            int: _description_
        """
        sliding_window_list = []
        dict_sliding_window = {}
        max_sum = 0
        for num in nums:
            print(sliding_window_list)
            if len(sliding_window_list) < k:
                sliding_window_list.append(num)
                if num in dict_sliding_window.keys():
                    dict_sliding_window[num] += 1
                else:
                    dict_sliding_window[num] = 1

            elif len(sliding_window_list) == k:
                print(sliding_window_list)
                if self.check_condition(dict_sliding_window, k):
                    print(dict_sliding_window)
                    sum_window = sum(sliding_window_list)
                    if sum_window > max_sum:
                        max_sum = sum_window
                    # list_sub_arays.append(sliding_window_list)
                first_element_sliding_window = sliding_window_list[0] 
                sliding_window_list = sliding_window_list[1:]
                sliding_window_list.append(num)
                self.update_dict_sliding_window(dict_sliding_window, first_element_sliding_window, num)
        
        if self.check_condition(dict_sliding_window,k):
            # list_sub_arays.append(sliding_window_list)
            sum_window = sum(sliding_window_list)
            if sum_window > max_sum:
                max_sum = sum_window
        
        return max_sum
    
    def maximumSubarraySum(self, nums, k):
        """This solution provied by someone else, it's faster.

        Args:
            nums (_type_): _description_
            k (_type_): _description_

        Returns:
            _type_: _description_
        """
        l, r = 0, 0
        mx, total = 0, 0
        visit = set()
        while r < len(nums):
            while nums[r] in visit:
                total -= nums[l]
                visit.remove(nums[l])
                l += 1
            total += nums[r]
            visit.add(nums[r])
            if (r - l + 1) == k:
                mx = max(mx, total)
                total -= nums[l]
                visit.remove(nums[l])
                l += 1

            r += 1
        return mx



x = Solution()
nums = [1,5,4,2,9,9,9]
k = 3
print(x.maximumSubarraySum(nums, k))