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

def reverse_list(head):
    new_head = None
    while head:
      head.next, head, new_head = new_head, head.next, head
    return new_head
