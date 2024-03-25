
"""
When the recursive call is made after the loop, it results in a different traversal order known as "post-order traversal"(BFS manner). In post-order traversal, the nodes are recursively visited in the following order:
1. Traverse the left subtree in post-order.
2. Traverse the right subtree in post-order.
3. Visit the current node

This traversal technique is called "post-order" because the current node is visited after its child nodes. Here is the example:
     1
    / \
   2   3
  / \
 4   5

In post-order traversal, the order of node visits would be: 4 -> 5 -> 2 -> 3 -> 1.

Post-order traversal is commonly used in deleting a tree from memory, evaluating postfix notation in mathematical expressions, and expression trees. 

Another example in Python to illustrate in-order traversal when the recursive call is made inside the loop:


             level 2
          /     |     \     
    node 0   node 1   node 2

             level 1
          /     |     \     
    node 0   node 1   node 2

You can run the script to see the result :
"""



# Function for post-order traversal (BFS manner)
def post_order_bfs(level):
    if level > 0:
        for node in range(3):
            print("Post-order Inside Loop Level {}, node {}".format(level,node))
        
        # Recursive call after the loop
        post_order_bfs(level - 1)
        
        print("Post-order Level:", level)


# Output of the function for in-order traversal
print("Post-order Traversal:")
post_order_bfs(2)