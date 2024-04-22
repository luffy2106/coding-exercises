"""
Problem:
https://leetcode.com/problems/kth-largest-element-in-an-array/description/


Solution:
Need to review heap first.
- From array, convert it to heap max, this step take 0(log N)
- Because it heap max, the element in the top alway bigger than the child => we can print the largest K
"""


from typing import List
import heapq


class PQEntry:
    """
    Create max heap, need to redefine the __lt__ operator because the default of heapq is min heap
    """
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value > other.value
    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for number in nums:
            heapq.heappush(heap, PQEntry(number))
        count=1
        top_heap_k = 0
        while count<=k:
            top_heap_k = heapq.heappop(heap)
            count+=1
        return top_heap_k.value
def main():
    nums = [3,2,1,5,6,4] 
    k = 2
    s =  Solution()
    heap_max = s.findKthLargest(nums,k)
    print(heap_max)
    # print(max_k)






if __name__ == "__main__":
    main()