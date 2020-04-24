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

input = ListNode(1)
input.next = ListNode(2)
input.next.next = ListNode(3)
input.next.next.next = ListNode(4)
input.next.next.next.next = ListNode(5)

head_rl = reverse_ll(input)
while head_rl: 
    print(head_rl.val)
    head_rl = head_rl.next 
    