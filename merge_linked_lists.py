""" 
  P    C
 l1:   1 -> 6 -> 7 -> 8 
        N 
 l2:    2 -> 3 -> 4 -> 5 -> 9 -> 10 

The idea is to insert the nodes of the second linked list into the first one. 
In order to perform this we keep track of three pointers: 
    1) prevNode (points to the previous node in the insertion list)
    2) currentNode (points to the current node in the insertion list)
    3) nodeToInsert (points to the current node in the list to insert from) 

At each iteration, we compare the value of the currentNode to the nodeToInsert. 
If currentNode.value < nodeToInsert.value we increment the currentNode and prevNode pointers, as the currentNode is in correct position
If currentNode.value > nodeToInsert.value we insert the nodeToInsert behind currentNode and update pointers. 

When we are done, we can check if we have any more nodes to insert in the insertion list. 
We simply validate this by checking the content of nodeToInsert and point currentNode.next to whatsever left in nodeToInsert. 

""" 

class ListNode: 
    def __init__(self, value): 
        self.value = value 
        self.next = None 

def print_values(head): 
    while head:
        print(head.value)
        head = head.next 

def mergeLinkedLists(headOne, headTwo): 
    prevNode, currentNode, nodeToInsert = None, headOne, headTwo   

    while currentNode and nodeToInsert: 
        if currentNode.value < nodeToInsert.value: 
            # increment the pointers 
            prevNode = currentNode 
            currentNode = currentNode.next  
        else:
            if prevNode:
                prevNode.next = nodeToInsert 
            prevNode = nodeToInsert
            nodeToInsert = nodeToInsert.next 
            prevNode.next = currentNode

    if not currentNode: 
        prevNode.next = nodeToInsert 

    return headOne if headOne.value < headTwo.value else headTwo 

first = ListNode(1)
first.next = ListNode(3)

second = ListNode(2)
second.next = ListNode(4)

headOne = ListNode(2)
headOne.next = ListNode(6)
headOne.next.next = ListNode(7)
headOne.next.next.next = ListNode(8)

headTwo = ListNode(1)
headTwo.next = ListNode(3)
headTwo.next.next = ListNode(4)
headTwo.next.next.next = ListNode(5)
headTwo.next.next.next.next = ListNode(9)
headTwo.next.next.next.next.next = ListNode(10)

head = mergeLinkedLists(headOne, headTwo) 

print_values(head)

