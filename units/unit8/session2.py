class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

def is_univalued(root):
    
    # provide definitions
    target = root.val

    # an empty tree is uni-valued
    if not root:
        return True
     
    # recursive call a dfs
    def dfs(node, target):
        # node doesnt exist
        if not node:
            return True
        
        # if current value doesnt amtch target return false
        if node.val != target:
             return False
        
        # recursively check left and right subtrees
        return dfs(node.left, target) and dfs(node.right, target)
    
    return dfs(root, root.val)



root = TreeNode(1)
node_two = TreeNode(1)
node_three = TreeNode(1)
root.right = node_two
root.left = node_three

print(is_univalued(root))