

"""
https://leetcode.com/problems/reverse-linked-list-ii/submissions/1309632995/?envType=study-plan-v2&envId=top-interview-150

Solution:
- We need to store 3 nodes: 1 left_node to store the node in left index, 1 node pre_left which store the node before left index, 1 node next_right which store the node after right index
- We move from begin to left index, mark the position of left_node and pre_left 
- We move from left index to right index, mark the position of next_right(we reverse the pointer during the move)
- We plug the pre_left to current_node : pre_left.next = current_node
- We plug the left_node to next_right : left_node.next = next_right



"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Move to left index
        print(left)
        print(right)
        pre_node = None
        current_node = head
        print(head.val)
        for i in range(0, left):
            print("current node is {}".format(current_node.val))
            next_node = current_node.next
            pre_node = current_node
            current_node = next_node
            # print("pre node is {}".format(pre_node.val))

        # print("left node is {}".format(current_node.val))
        left_node = current_node
        pre_left = pre_node


        # We move from left index to right index, mark the position of next_right(we reverse the pointer during the move)
        for j in range(left, right-1):
            next_node = current_node.next
            current_node.next = pre_node
            pre_node = current_node
            current_node = next_node    
        print("haha")
        next_right = current_node.next
        right_node = current_node
        pre_left.next = right_node
        left_node.next = next_right

        next_right = current_node.next

        return head





x =  Solution()
head = [1,2,3,4,5]
left = 2
right = 4
x.reverseBetween(head, left, right)


        
        

        

        

        

        