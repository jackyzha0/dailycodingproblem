class ListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next:
            return str(self.val) + " -> " + str(self.next)
        else:
            return str(self.val)

# 2.1 - remove dupes from linkedlist
def removeDupesLL(head):
    while head.val == head.next.val:
        head = head.next

    root = head
    while head and head.next:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next

    return root

# 2.1 Follow Up - no temp buffer

# 2.2 nth-to-last element of linkedlist

# 2.3 delete node given only access to node

# 2.4 sum 2 linkedlists element-wise

# 2.5 check for cycle in linkedlist
