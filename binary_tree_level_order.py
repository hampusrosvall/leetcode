import collections 

class TreeNode: 
    def __init__(self, value): 
        self.value = value 
        self.left, self.right = None, None 


"""
                    3 
                   / \ 
                  9   20 
                      / \
                     15  7 
""" 

# recursive implementation 
def levelOrderTraversal(root):
    nodesAtLevel = collections.defaultdict(list)

    def traverse(node, level): 
        if not node: return 

        nodesAtLevel[level].append(node.value) 
        traverse(node.left, level + 1)
        traverse(node.right, level + 1)

    traverse(root, 0)
    return nodesAtLevel.values()

# iterative BFS implementation 
def levelOrderBFS(root): 
    queue = [root]
    levels = []
    while queue: 
        levelQueue = list()
        levelList = list()
        for node in queue: 
            levelList.append(node.value)
            if node.left: levelQueue.append(node.left)
            if node.right: levelQueue.append(node.right)

        levels.append(levelList)
        queue = levelQueue

    return levels   

# iterative BFS more dense solution 
def levelOrderDense(root): 
    queue = [root]  
    levels = list()

    while queue: 
        nbrNodesAtLevel = len(queue)
        levelValues = list()
        for _ in range(nbrNodesAtLevel): 
            currentNode = queue.pop(0) # pretending that we have a LinkedList-like implementation to support O(1) pops 
            levelValues.append(currentNode.value)
            if currentNode.left: queue.append(currentNode.left) 
            if currentNode.right: queue.append(currentNode.right)

        levels.append(levelValues)

    return levels 

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(levelOrderDense(root))

