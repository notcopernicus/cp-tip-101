# problem one: build a binary tree

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# create nodes
root_node = TreeNode(10)
node_two = TreeNode(6)
node_three = TreeNode(4)

root_node.right = node_two
root_node.left = node_three

print(root_node.val , 'is the root node')
print(node_two.val, ' to the right')
print(node_three.val, ' to the left')

# problem two: 3 node sum

# if root == sum(node_one.val, node_two.val)
#     return true
# otherwise, return false

# def check_tree(root_node):

#     if root_node.right.val + root_node.left.val == root_node.val:
#         return True
#     return False

# print (check_tree(root_node))

def check_tree(root_node):
    # check if children are NONE
    if not root_node.left or not root_node.left:
        return False
    # only return true if we can add children (since they exist)
    return root_node.left.val + root_node.right.val == root_node.val

print (check_tree(root_node))