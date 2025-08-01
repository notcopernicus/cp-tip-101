# Problem 1: Level Order Traversal of Binary Tree

# Given the following pseudocode and the root of a binary tree, return a list 
# of the level order traversal of it’s nodes’ values (i.e., from left to right, level by level).


from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_order(root):

    # create empty list
    lst = []

    # If the tree is empty:
    if not root:
        return lst
    # return an empty list

    # Create an empty queue using deque
    queue = deque()

    # Add the root to the queue
    queue.append(root)

    # While the queue is not empty:
    while not queue: 
    # Pop the next node off the queue (pop from the left side!)
        removed = queue.popleft()
    # Add the popped node to the list of explored nodes
        lst.append(removed)
    # Add each of the popped node's children to the end of the queue
        queue.append(removed.right)
        queue.append(removed.left)
    # Return the list of visited nodes
        return lst


# test case
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.right = TreeNode(3)
root.left.left = TreeNode(1)

print(level_order(root))