class ListNode: 
    def __init__(self, value): 
        self.val = value 
        self.next = None 

def merge_lists(l1: ListNode, l2: ListNode):
    dummy_head = ListNode(0)
    curr_first = l1 
    curr_second = l2 
    node = dummy_head 

    while curr_first and curr_second: 
        if curr_first.val <= curr_second.val: 
            node.next = ListNode(curr_first.val)
            curr_first = curr_first.next 
        else: 
            node.next = ListNode(curr_second.val)
            curr_second = curr_second.next 

        node = node.next 

    while curr_first: 
        node.next = ListNode(curr_first.val) 
        node = node.next 
        curr_first = curr_first.next 

    while curr_second: 
        node.next = ListNode(curr_second.val)
        node = node.next 
        curr_second = curr_second.next 

    return dummy_head.next 

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

head = merge_lists(l1, l2)

while head: 
    print(head.val)
    head = head.next 

