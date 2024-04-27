"""
I. Question 
https://leetcode.com/problems/reverse-linked-list/description/

Given the head of a singly linked list, reverse the list, and return the reversed list.
Ex1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Ex2:
Input: head = [1,2]
Output: [2,1]

Ex3:
Input: head = []
Output: []
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while current is not None:
            next_node = current.next # This line stores a reference to the next node in the original linked list. It is crucial to store this reference before updating the current node's next pointer to point to the previous node.
            current.next = prev # he next pointer of the current node is updated to point to the prev node. By doing this, the direction of the link is reversed, connecting the current node to the prev node instead of its original successor.
            prev = current # After updating the current node's next pointer, the prev pointer is moved forward to the current node. This prepares the prev node for the next iteration, where it will become the new current node.
            current = next_node # Finally, the current pointer is updated to move to the next node in the original list (previously stored in next_node). This progression allows the algorithm to continue traversing the original linked list while reversing the links between nodes.
        return prev
        

"""
The following solution is wrong because when you use list to store the the element, the address in the 
memory will be messed
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        reversed_node = None
        previous = None
        while current is not None:
            previous = current
            # print(previous.val)
            current = current.next
            # print(previous.val)
            if current is not None:
                # print(current.val)
                reversed_node = ListNode(current.val, previous)
                
        return reversed_node