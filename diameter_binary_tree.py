class TreeNode: 
    def __init__(self, value): 
        self.val = value 
        self.left = None 
        self.right = None 

""" 
Time: O(N)
Space:
    - Best case: O(log N)
    - Worst case: O(N) (imbalanced tree)

This question is rather tricky for being an easy question. 
The intuition behind the solution is to, at every node, retrieve the left and right depth of the children nodes. 
We then set the diameter to be the maximum of the current observed diamater and the sum of the right and left subtrees. 

The tree is traversed in a "depth first" manner, where we increment the depth going upwards in the recursive call stack. 

        diameter = max(diameter, left + right)
                        1 diameter = max(diameter, 3 + 0) = 4 
                       / 
                      2 2->1: return 1 + max(2, 2), diamter = max(diameter, 2 + 2) = 4
                     / \    
                    3   4 3->2: return 1 + max(1, 0), diameter = 1, 4->2: return 1 + max (0, 1), diameter = 1
                   /     \ 
                  7       5 7->3: return 1 + max(0, 0), diameter = 0, 5->4: return 1 + max(0,0) dimater = 1

"""  
class Solution: 
    def diameterOfBinaryTree(self, root: TreeNode) -> int: 
        self.diameter = 0 
        self.exploreTree(root) 
        return self.diameter  

    def exploreTree(self, node): 
        if not node: return 0 

        # calculate the depth of the children nodes 
        leftDepth = self.exploreTree(node.left)
        rightDepth = self.exploreTree(node.right)

        # return the current depth of the node 
        self.diameter = max(self.diameter, leftDepth + rightDepth)
        return 1 + max(leftDepth, rightDepth)

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.right = TreeNode(5)

sol = Solution()
print(sol.diameterOfBinaryTree(root))