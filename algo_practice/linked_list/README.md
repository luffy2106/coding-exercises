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
- Singly Linked List
- Doubly Linked List
- Circular Linked List
- Circular Doubly Linked List
- Header Linked List

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

### Practice exercices need to focuse
```
https://www.geeksforgeeks.org/top-20-linked-list-interview-question/?ref=lbp
```