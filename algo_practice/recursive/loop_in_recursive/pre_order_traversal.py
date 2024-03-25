
"""
When the recursive call is made before the loop, it results in a different traversal order known as "pre-order traversal"(DFS manner). In pre-order traversal, the nodes are recursively visited in the following order:

Visit the current node.
Traverse the left subtree in pre-order.
Traverse the right subtree in pre-order.
This traversal technique is called "pre-order" because the current node is visited before its child nodes. Here's a simple example of pre-order traversal:

     1
    / \
   2   3
  / \
 4   5


In pre-order traversal, the order of node visits would be: 1 -> 2 -> 4 -> 5 -> 3.

Another example in Python to illustrate in-order traversal when the recursive call is made inside the loop:


             level 2
          /     |     \     
    node 0   node 1   node 2

             level 1
          /     |     \     
    node 0   node 1   node 2

You can run the script to see the result :
Pre-order Traversal:
Pre-order Level: 2
Pre-order Level: 1
Pre-order Inside Loop Level 1, node 0
Pre-order Inside Loop Level 1, node 1
Pre-order Inside Loop Level 1, node 2
Pre-order Inside Loop Level 2, node 0
Pre-order Inside Loop Level 2, node 1
Pre-order Inside Loop Level 2, node 2
"""


# Function for pre-order traversal (DFS manner)
def pre_order_dfs(level):
    if level > 0:
        print("Pre-order Level:", level)
        
        # Recursive call before the loop
        pre_order_dfs(level - 1)
        
        for node in range(3):
            print("Pre-order Inside Loop Level {}, node {}".format(level,node))



# Output of the function for in-order traversal
print("Pre-order Traversal:")
pre_order_dfs(2)