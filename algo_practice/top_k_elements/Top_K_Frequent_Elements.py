"""
Problem:
https://leetcode.com/problems/top-k-frequent-elements/description/


Solution:
Need to review heap first.
- From array, convert it to heap max, this step take 0(log N)
- Because it heap max, the element in the top alway bigger than the child => we can print the largest K
"""

import heapq
from typing import List

class PQEntry:
    """
    Create max heap, need to redefine the __lt__ operator because the default of heapq is min heap
    """
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value > other.value

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap_frequent = []
        top_k_frequent = []
        dict_frequency = {}
        for num in nums:
            if num in dict_frequency.keys():
                dict_frequency[num] += 1
                heapq.heappush(heap_frequent, PQEntry(dict_frequency[num]))
            else:
                dict_frequency[num] = 1
                heapq.heappush(heap_frequent, PQEntry(dict_frequency[num]))
        for i in range(k):
            top_k_frequent.append(heapq.heappop(heap_frequent).value)
        return top_k_frequent
