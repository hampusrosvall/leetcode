"""
I think it's simple to when traversing and manipulating LinkedLists to keep two (in some cases more) pointers in order to perform clean manipulations.
The idea behind this algorithm is to first move the head to a position where the value of the head is not equal to the value to remove, this is done in the first while loop.
If we still have nodes to traverse, we continue else we return a None-pointer.

In order to traverse the rest of the list, two pointers are initialized, one to the previous node (in this case it is initialized to the head) and one to the node next of the head. 
If we encounter a node where the value of the node is equal to the value to remove. We simply change the previous node's next property to point to the current node's next property. 
Otherwise, we shift the pointers one step to the right in the LinkedList.

Thus, this algorithm runs in O(N) time and O(1) space as we visist all the nodes in the LinkedList, and no extra memory is allocated except two pointers (which doesn't scale with the number of input elements).


"""

class ListNode: 
    def __init__(self, val): 
        self.val = val 
        self.next = None 


def removeElements(head: ListNode, val: int) -> ListNode: 
    if not head: return None 

    while head and head.val == val: 
        head = head.next 

    prevNode, currentNode = head, head   

    while currentNode: 
        if currentNode.val == val: 
            prevNode.next = currentNode.next 

        prevNode = currentNode 
        currentNode = currentNode.next 


    return head  

def print_values(head: ListNode): 
    while head: 
        print(head.val)
        head = head.next 

head = ListNode(1)
print_values(removeElements(head, 1))



