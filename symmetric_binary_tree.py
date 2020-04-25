class Solution: 
    def isSymmetric(self, root): 
        if not root: return True 

        return self.validateSym(root.left, root.right)

    def validateSym(self, left, right): 
        if not left and not right: return True 
        if not left or not right: return False 
        if left.val != right.val: return False 

        return self.validateSym(left.left, right.right) and self.validateSym(left.right, right.left)