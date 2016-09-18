class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse_list_nondestructive(head):
    new_head = None
    while head:
        new_head = Node(head.value, new_head)
        head = head.next
    return new_head

# another implementation I made while practicing whiteboarding
def rev_ll_nd2(head):
    cur = Node(head.value, None)
    while head.next:
        cur = Node(head.next.value, cur)
        head = head.next
    return cur

def reverse_list(head):
    new_head = None
    while head:
      head.next, head, new_head = new_head, head.next, head
    return new_head

# another implementation from whiteboarding practice
def rev_list2(head):
    nxt = None
    while head:
        head.next, head, nxt = nxt, head.nxt, head

# just helper functions for testing
def make_test_list():
    cur = Node(10, None)
    for i in range(9, 0, -1):
        cur = Node(i, cur)
    return cur

def print_list(head):
    cur = head
    print cur.value
    while cur.next:
        cur = cur.next
        print cur.value

if __name__ == "__main__":
    head = make_test_list()
    print('original linked list')
    print_list(head)

    nd_head = reverse_list_nondestructive(head)
    print('non destructive linked list reversal')
    print_list(nd_head)
    print('og linked list still there')
    print_list(head)

    dest_head = reverse_list(head)
    print('destructive linked list reversal')
    print_list(dest_head)
    print('og linked list now reversed')
    print_list(head)

    head2 = make_test_list()
    nd_head2 = rev_ll_nd2(head2)
    print('non destructive linked list reversal 2')
    print_list(nd_head2)
    print('og linked list still there')
    print_list(head2)

    dest_head2 = reverse_list(head2)
    print('destructive linked list reversal 2')
    print_list(dest_head2)
    print('og linked list now reversed')
    print_list(head2)
