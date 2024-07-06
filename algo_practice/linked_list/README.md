# Linked List 

A linked list is a linear data structure that consists of a series of nodes connected by pointers. Each node contains data and a reference to the next node in the list. Unlike arrays, linked lists allow for efficient insertion or removal of elements from any position in the list, as the nodes are not stored contiguously in memory.

The difference between Linked List and Array:

Linked List:
- Data Structure: Non-contiguous
- Memory Allocation: Dynamic
- Insertion/Deletion: Efficient
- Access: Sequential
Array:
- Data Structure: Contiguous
- Memory Allocation: Static
- Insertion/Deletion: Inefficient
- Access: Random

### Types of linked list
- Singly-Linked List consists of nodes, starting from head node to NULL, where each node contains a data field and a next pointer.
- Doubly-Linked List consists of nodes, where each node contains a data field, a next pointer and a prev pointer.
- Circular Linked List is similar to a singly-linked list except that the last node instead of connecting to NULL connects to the first node, creating a ring.
- Circular Doubly-Linked List is a mixture of the circular and doubly-linked list which has two pointers prev and next, and the last node connects to the first node.
- Multi-Linked List consists of nodes, where each node contains a data field and two or more pointers. A doubly-linked list is a special case of the multi-linked list, which has two pointers that are the exact inverse of each other. These lists are typically used to implement different sorting of the nodes. For example, given student names and their marks, one set of pointers will sort by name and the other set by marks.


### Setup of linked list
The setup of the linked list alway has 2 main elements:
- Node(which include data and the pointer to the next node)
- LinkedList(which is the head of the linked list)

```
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None # Head of the list
```



### Operations of Linked Lists
- Linked List Insertion
- Search an element in a Linked List (Iterative and Recursive)
- Find Length of a Linked List (Iterative and Recursive)
- Reverse a linked list
- Linked List Deletion (Deleting a given key)
- Linked List Deletion (Deleting a key at given position)
- Write a function to delete a Linked List
- Write a function to get N_th node in a Linked List
- N_th node from the end of a Linked List


### Implementation steps

https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/

### Practice exercices need to focuse
```
https://www.geeksforgeeks.org/top-20-linked-list-interview-question/?ref=lbp
```