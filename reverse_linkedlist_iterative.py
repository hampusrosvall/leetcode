class ListNode: 
    def __init__(self, value): 
        self.val = value 
        self.next = None 

""" 
Time: O(N) as we perform a linear scan of the input list 
Memory: O(N) as we allocate nodes in reverse order of the input list  

Idea behind approach: 

input linked list: 1 -> 2 -> 3 -> 4 -> 5 
                   ^

we traverse the input linked list from left -> right and for each node that is not None we perform the following steps: 
    1) Create a new node in the reversed list with the value of the current node in the input linked list 
    2) Point that node to the previous created node in the reversed list 
    3) Update pointers
""" 

def reverse_ll(head): 
    prev_rl = None # initialize the previously created node to None as the tail has no next node 
    node_ll = head # initialize pointer to current node in the input linked list 

    while node_ll: 
        current_rl = ListNode(node_ll.val)
        current_rl.next = prev_rl 
        prev_rl = current_rl 
        node_ll = node_ll.next 

    return prev_rl 

""" 
Reverse Linked List in O(1) memory 

Consider the input: 1 -> 2 -> 3 -> 4 -> 5  

The trick here is to basically keep three pointers for each iteration and then repoint the nodes inplace. 

The pointers needed are:
                1) currentPointer(C) (points to the current node)
                2) prevPointer(P) (points to the previous node)
                3) nextPointer(N) (points to the next node)

For each node we perform: 
        1) Store nextPointer as currentPointer.next 
        2) Repoint currentPointer.next to prevPointer 
        3) Set prevPointer to currentPointer
        4) Set currentPointer to nextPointer 

Hence, we are rearranging pointers in place. 

Consider the case when the currentPointer is at the second node. 

    1 -> 2 -> 3 -> 4 -> 5  ==> 2 -> 1 ; 3 -> 4 -> 5 ==> 3 -> 2 -> 1 ; 4 -> 5 ==> 4 -> 3 -> 2 -> 1 ; 5 
    P    C    N                P        C    N         P              C    N     P                  C  N is None 
 
The algorithm runs in O(N) time and O(1) space 

""" 

def reverseConstantSpace(head): 
    prevPointer, currentPointer = None, head 

    while currentPointer: 
        nextPointer = currentPointer.next 
        currentPointer.next = prevPointer
        prevPointer = currentPointer 
        currentPointer = nextPointer

    return prevPointer 

input = ListNode(1)
input.next = ListNode(2)
input.next.next = ListNode(3)
input.next.next.next = ListNode(4)
input.next.next.next.next = ListNode(5)

head_rl = reverse_ll(input)
print('====== LINEAR SPACE ======')
while head_rl: 
    print(head_rl.val)
    head_rl = head_rl.next 

head_rlcs = reverseConstantSpace(input)
print('====== CONSTANT SPACE ======')
while head_rlcs: 
    print(head_rlcs.val)
    head_rlcs = head_rlcs.next 