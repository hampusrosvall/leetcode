class TreeNode: 
    def __init__(self, value): 
        self.val = value 
        self.left = None 
        self.right = None 

def max_depth(root: TreeNode) -> int: 
    return max_depth_recursive(root, 0)

def max_depth_recursive(node: TreeNode, depth: int): 
    if not node: 
        return depth

    return max(max_depth_recursive(node.left, depth + 1), max_depth_recursive(node.right, depth + 1))

tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

""" 
    3
   / \
  9  20
    /  \
   15   7
""" 

print(max_depth(tree))