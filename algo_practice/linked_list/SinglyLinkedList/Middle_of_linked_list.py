"""
1. Question 
https://leetcode.com/problems/middle-of-the-linked-list/description/

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Ex1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Ex2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

2. Solution
- count the total number of nodes in the list by traversing it once. 
- Then, we calculate the index of the middle node.
- we traverse the list again from the beginning to reach the middle node and return it
"""

from typing import Optional

    

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. We first count the total number of nodes in the list by traversing it once. 
        count = 0
        current = head
        while current:
            count+=1
            current = current.next
        # 2. Then, we calculate the index of the middle node
        mid = count//2
        # 3. We traverse the list again from the beginning to reach the middle node and return it
        current =  head
        for i in range(mid):
            current = current.next
        return current
