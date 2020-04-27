def isPalindromeExtraSpace(head): 
    if not head or not head.next: return True 
    
    cache = list()

    currentNode = head 

    while currentNode: 
        cache.append(currentNode.val)
        currentNode = currentNode.next 
    
    left = 0 
    right = len(cache) - 1 

    while left < right: 
        if cache[left] != cache[right]: return False 

        left -= 1 
        right += 1 

    return True 

def isPalindromeStack(head): # stores N/2 elements instead of N (still O(N)) however 
    if not head or not head.next: return True
    if not head.next.next: return head.val == head.next.val 

    # find the middle of the array 
    turtoise, hare = head, head 
    stack = []

    while hare and hare.next: 
        stack.append(turtoise.val)
        turtoise = turtoise.next 
        hare = hare.next.next 

    # if hare is not None after the while loop we have odd number of nodes 
    valNode = turtoise.next if hare else turtoise

    while len(stack): 
        value = stack.pop()
        if value != valNode.val: return False 
        valNode = valNode.next 

    return True 

    





    
