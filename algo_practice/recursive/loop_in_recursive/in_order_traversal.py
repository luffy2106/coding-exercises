

"""
When the recursive call is made inside the loop, it results in a different traversal order known as "in-order traversal". In in-order traversal, the recursive calls are made between processing the left subtree and the current node, resulting in a specific order of traversal.

Here's an example :

       1
      / \
     2    3
    / \  / \
   4   5 7  8

In-order traversal of the above binary tree would visit the nodes in the following order: 4 -> 2 -> 5 -> 1 -> 3 -> 7 ->8. This sequence reflects the left subtree being visited first, followed by the current node, and then the right subtree.


Another example in Python to illustrate in-order traversal when the recursive call is made inside the loop:


             level 2
          /     |     \     
    node 0   node 1   node 2

             level 1
          /     |     \     
    node 0   node 1   node 2

You can run the script to see the result :

In-order Traversal:
In-order Inside Loop Level: 2, node 0
In-order Inside Loop Level: 1, node 0
In-order Inside Loop Level: 1, node 1
In-order Inside Loop Level: 1, node 2
In-order Level: 1
In-order Inside Loop Level: 2, node 1
In-order Inside Loop Level: 1, node 0
In-order Inside Loop Level: 1, node 1
In-order Inside Loop Level: 1, node 2
In-order Level: 1
In-order Inside Loop Level: 2, node 2
In-order Inside Loop Level: 1, node 0
In-order Inside Loop Level: 1, node 1
In-order Inside Loop Level: 1, node 2
In-order Level: 1
In-order Level: 2

"""


# Function for in-order traversal
def in_order_traversal(level):
    if level > 0:
        for i in range(3):
            print("In-order Inside Loop Level: {}, node {}".format(level,i))
            
            # Recursive call inside the loop
            in_order_traversal(level - 1)
        
        print("In-order Level:", level)

# Output of the function for in-order traversal
print("In-order Traversal:")
in_order_traversal(2)
