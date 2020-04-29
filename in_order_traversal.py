def inOrderRecursive(root): 
    nodeValues = []

    def helper(root): 
        if not root: return 
        helper(root.left)
        nodeValues.append(root.value)
        helper(root.right)

    helper(root)

    return nodeValues 

def inOrderIterative(root): 
    currentNode = root 
    stack = list()
    nodeValues = list()
    while currentNode or len(stack): 
        while currentNode: 
            stack.append(currentNode)
            currentNode = currentNode.left

        currentNode = stack.pop()
        nodeValues.append(currentNode.value)
        currentNode = currentNode.right 

    return nodeValues 