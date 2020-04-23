class ListNode:
    def __init__(self, value):
        self.val = value 
        self.next = None 
        

def add_two_numbers(l1, l2): 
    dummy = ListNode(0)
    p, q, curr = l1, l2, dummy 
    carry = 0 
    
    while p or q: 
        p_val = p.val if p else 0 
        q_val = q.val if q else 0 
        node_sum = p_val + q_val + carry 
        
        if node_sum >= 10: 
            carry = 1 
            node_sum %= 10 
        else: 
            carry = 0 

        # we add the nodes to dummyhead.next to achieve a simple logic inside the while block
        curr.next = ListNode(node_sum)
        curr = curr.next

        if p: p = p.next
        if q: q = q.next

    if carry:
        curr.next = ListNode(1)
        
    return dummy
    
    
l1 = ListNode(2)
l1.next = ListNode(4) 
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

add_two_numbers(l1, l2)
