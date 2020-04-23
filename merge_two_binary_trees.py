class TreeNode: 
    def __init__(self, value): 
        self.val = value 
        self.left = None 
        self.right = None 
""" 

Explanation to the if not statements at the very top of the merge_trees function. 
If the first_tree or second_tree is None, we append the whole branch given any level in the merged tree. 

E.g., given the scenario below: 
 
                first_tree:    second_tree:               merged_tree: 
                     2              1                          3  
                    /                \                        / \
                   5                 18                      5   18 
                  /                    \                    /     \
                 7                      20                 7      20

Since the first_tree has no right branch, we will return the whole branch of the second tree, and vice versa. 
""" 
def merge_trees(first_tree, second_tree): 
    if not first_tree: return second_tree
    if not second_tree: return first_tree 

    first_tree.val += second_tree.val 

    first_tree.left = merge_trees(first_tree.left, second_tree.left)
    first_tree.right = merge_trees(first_tree.right, second_tree.right)

    return first_tree  

def in_order(node): 
    if node: 
        in_order(node.left)
        print(node.val)
        in_order(node.right)

""" 
        first_tree                 second_tree                     merged_tree 
            1                           2                              3 
           / \                         / \                            /  \
          3   2                       1   3                          4    5 
         /                             \   \                        / \    \  
        5                              4    7                      5   4    7  
       /                                                          /
      7                                                          7 

in_order_traversal should yield: 7 5 4 4 3 5 7 
"""

first_tree = TreeNode(1)
first_tree.left = TreeNode(3)
first_tree.right = TreeNode(2)
first_tree.left.left = TreeNode(5)
first_tree.left.left.left = TreeNode(7)

second_tree = TreeNode(2)
second_tree.left = TreeNode(1)
second_tree.right = TreeNode(3)
second_tree.left.right = TreeNode(4)
second_tree.right.right = TreeNode(7)
second_tree.right.right.right = TreeNode(18)

merged_root = merge_trees(first_tree, second_tree)

in_order(merged_root)




