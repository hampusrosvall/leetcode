class TreeNode: 
    def __init__(self, value): 
        self.val = value 
        self.left = None 
        self.right = None 

import collections

""" 
This question is rather tricky as we need to keep track of several sums simultaneously. 
However, we make use of storing the current path sums in a hashmap where we increment the current observed sum by one each time 
that path, leading up to the given current_sum, is crossed in the tree. 

Consider the example below: 

                                          10 
                                         /
                                        5
                                      / 
                                     5
                                    /
                                   3 

If we are looking for the target 8, there is a path such that currentSum - someOldPathSum = target <=> currentSum - target = someOldPathSum
In this case, when we are at the leaf node 3, the currentSum is 23 and we need to look up the frequency of someOldPathSum which is 15. 
The sum 15 has occurred once so far along this path in the binary tree. And we know that there is one path leading to the target 8. 

As far as space-time complexity is concerned. We allocate atmost O(N) extra space if we have the situation as above. 
We traverse all the nodes leading to a O(N) time complexity.

When we are done exploring a path given a currentSum we need to decrement the frequency cache so that we don't explore that path again. 

E.g., consider the example below and the target -1: 

                                  1 
                                 / \
                               -2  -3 
Given the left subtree we have the following cache: {0:1, -1: 1} and we have 1 -> -2 which leads to -1. 
If we don't update the cache, when we are traversing the right subtree we will look for the frequency of 
currentSum - target = -2 - (-1) = -1 and we will increment the counter of valid paths falsely. 

"""  

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.n_paths = 0 
        
        cache = collections.defaultdict(int)
        cache[0] += 1 
        
        self.findPathsRecursive(root, 0, cache, sum)
        
        return self.n_paths
    
    def findPathsRecursive(self, node, current_sum, cache, target): 
        if not node: return 
        
        current_sum += node.val 
        self.n_paths += cache[current_sum - target]
        cache[current_sum] += 1 
        self.findPathsRecursive(node.left, current_sum, cache, target)
        self.findPathsRecursive(node.right, current_sum, cache, target)
        cache[current_sum] -= 1 

sol = Solution()

root = TreeNode(1)
root.left = TreeNode(-2)
root.right = TreeNode(-3)

sol.pathSum(root, -1)

