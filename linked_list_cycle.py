""" 
Time: O(N) 
Space: O(N) as we are using a hashset to store the visited nodes 

""" 

def findLoopExtraMemory(head): 
    if not head: return False 

    cache = set()
    currentNode = head 

    while currentNode: 
        if currentNode in cache: return True 

        cache.add(currentNode)
        currentNode = currentNode.next  

    return False 

""" 
This problem can be solved in O(1) memory using two pointers. 
We can make use of a turtoise and hare technique where the hare travels twice as fast as the turtoise. 

If we reach a point where the two pointers point to the same node, we know we have a cycle. 
If the turtoise reaches None then we don't have a cycle. 

""" 

def findLoopTwoPointers(head): 
    if not head or not head.next: return False 

    turtoise = head.next 
    hare = head.next.next 

    while turtoise != hare: 
        if not hare or not hare.next: return False 

        turtoise = turtoise.next 
        hare = hare.next.next 

    return True 

