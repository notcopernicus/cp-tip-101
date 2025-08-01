# problem one

''' we define non symmetry as a value being in the same 
position respective to a left and right subtree

traverse through the tree to ensure this definition

return False if non symmetric otherwise return True'

if root.left.val != root.right.val 
if root.left.val == root.right.val '''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root):
    # no value can be mirrored therefore must be True
    if not root:
        return True
    
    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val and
                is_mirror(t1.left, t2.right) and
                is_mirror(t1.right, t2.left))
    
    return is_mirror(root.left, root.right)
    

root = TreeNode(1)
node_two = TreeNode(2)
node_three = TreeNode(1)
root.right = node_two
root.left = node_three

print(is_symmetric(root))
    
