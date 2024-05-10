"""
Problem:
https://leetcode.com/problems/top-k-frequent-elements/description/

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

Solution:
Need to review heap first.
- Build a dict frequency with the key is the number and the value is the occurence of that number. At the same time, build heap to store the frequency of number in descending order
(it will take O(n))
- reverser the dict frequency, so we have the key which is the occurence and the value is the number (it will take O(n)) 
- From the reversered dict frequency and the heap max, we can print the list of top-k-frequent-elements  (it will take O(k))

The solution have O(n) complexity which is better than O(n log n)
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
        # Build a dict frequency with the key is the number and the value is the occurence of that number
        for num in nums:
            if num in dict_frequency.keys():
                dict_frequency[num] += 1
                heapq.heappush(heap_frequent, PQEntry(num))
            else:
                dict_frequency[num] = 1
                heapq.heappush(heap_frequent, PQEntry(num))
        # Convert key to value and value to key in dict_frequency
        dict_frequency_reversed = {dict_frequency[num]:num for num in dict_frequency.keys()}


        for i in range(k):
            top_frequency = heapq.heappop(heap_frequent).value
            key_top_frequency = dict_frequency_reversed[top_frequency]
            top_k_frequent.append(key_top_frequency)
        return top_k_frequent
