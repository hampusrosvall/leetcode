def TreeNode: 
    def __init__(self, value): 
        self.val = value 
        self.left = None 
        self.right = None 


def invert_binary_tree(tree): 
    if not tree: return 

    tree.left, tree.right = tree.right, tree.left 

    swap_branches(tree.left) 
    swap_branches(tree.right)

    return tree 

def swap_branches(node): 
    if not node: return 
    elif not node.left and not node.right: return 

    node.left, node.right = node.right, node.left 
    swap_branches(node.left)
    swap_branches(node.right) 


tree = TreeNode(4)
tree.left = TreeNode(2)
tree.right = TreeNode(7)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(9)