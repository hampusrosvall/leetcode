class TreeNode: 
    def __init__(self, value): 
        self.value = value 
        self.left, self.right = None, None 

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
        
        
        
            
        


array = [-10, -3, 0, 5, 9]
sortedArrayToBST(array)

    