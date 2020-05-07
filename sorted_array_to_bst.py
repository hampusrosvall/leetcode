class TreeNode: 
    def __init__(self, value): 
        self.value = value 
        self.left, self.right = None, None 

# this solution works, however at each recursive call we allocate extra memory causing the space complexity to be 
# O(N log N)
# passing pointers to left and right idx is cheaper, taking down the space complexity to O(log N)
class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        if not nums: return None 
        middle = len(nums) // 2 
        
        root = TreeNode(nums[middle])
        
        root.left = self.constructTree(nums[:middle])
        root.right = self.constructTree(nums[middle + 1:])
        
        return root 
        
    def constructTree(self, array): 
        if len(array) == 1: return TreeNode(array[0])
        elif not array: return None 
        
        middle = len(array) // 2

        node = TreeNode(array[middle])
        node.left = self.constructTree(array[:middle])
        node.right = self.constructTree(array[middle + 1:])
        
        return node 
        
# Space: O(log N)
# Time: 
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None 
        middle = len(nums) // 2 
        
        root = TreeNode(nums[middle])
        
        root.left = self.constructTree(nums, 0, middle - 1)
        root.right = self.constructTree(nums, middle + 1, len(nums) - 1)
        
        return root 
        
    def constructTree(self, array, left, right): 
        if left == right: return TreeNode(array[left])
        elif left > right: return None 
        
        middle = (left + right + 1) // 2 

        node = TreeNode(array[middle])
        node.left = self.constructTree(array, left, middle -1)
        node.right = self.constructTree(array, middle + 1, right)
        
        return node 
        
        
        
            
        
    