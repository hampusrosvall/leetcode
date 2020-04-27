"""
    1 -> 3 -> 5 -> 7 -> 9 -> 11 -> None 
                        B                                                      
    2 -> 4 -> 9 -> 11 -> None 
              A                                       

""" 

# using pointers 
def intersectLinkedPoint(headA, headB): 
    if not head A or not headB: return None 

    currentA = headA
    currentB = headB 

    while currentA != currentB: 
        currentA = currentA.next if currentA else headB 
        currentB = currentB.next if currentB else headA

    return currentA 

# using a hashset
def intersectLinkedMap(headA, headB): 
    visited = set()
    currentA = headA 
    while currentA: 
        set.add(currentA) 
        currentA = currentA.next 

    while currentB or currentB not in visited: 
        currentB = currentB.next 

    return currentB if currentB else None 
        
