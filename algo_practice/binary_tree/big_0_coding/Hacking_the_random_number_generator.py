"""
1. Question
You recently wrote a random number generator code for a web application and now you notice that some cracker has cracked it. It now gives numbers at a difference of some given value k more predominantly. You being a hacker decide to write a code that will take in n numbers as input and a value k and find the total number of pairs of numbers whose absolute difference is equal to k, in order to assist you in your random number generator testing.

NOTE: All values fit in the range of a signed integer, n, k>=1

Input
1st line contains n & k.
2nd line contains n numbers of the set. All the n numbers are assured to be distinct.

(Edited: n <= 10^5)

Output
One integer saying the number of pairs of numbers that have a diff k.

Ex :

Input:
5 2
1 5 3 4 2
Output:
3

Explain : We can see that there are 3 pairs which have diff k = 2: (1,3), (5,3), (4,2)


Source :

https://www.spoj.com/problems/HACKRNDM/

https://bigocoder.com/courses/138/lectures/1843/problems/1076?view=statement

2. Solution
- We can see that all integeres in the input has to be unique and we need to store the diff of unique value => we can use binary search tree
- Because in BST : left_node < mid_node < right_node, so we just need to see how many pairs (left_node, mid_node)/(mid_node/right_node) equal to k

Implementation:
Step 1 : Create a binary search tree from the list
Step 2 : For each node:
- If the root - root.left < 2, move to the left(if it's equal to 2 => count). When top_left = Node, stop
- If the root.right - root < 2, move to the right(if it's equal to 2 => count). When top_right = Node, stop
"""
import heapq
n, k = map(int, input().split())
a = list(map(int, input().split()))


n, k = 5,2
a = [1,5,3,4,2]

class PQEntry:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
      	return self.value > self.other
# 1. Build heapmax
heap_max = []      
for x in a:
    heapq.heappush(heap_max,PQEntry(x))

temp_list = []
while len(heap_max) > 0:    
    top = heapq.heappop(heap_max)
    temp_list.append(top.value)
    
