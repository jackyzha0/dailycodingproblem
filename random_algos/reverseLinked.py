# reverse singly linked list

class LinkedList():
    def __init__(self, val, next = None):
        self.x = val
        self.next = next

    def __str__(self):
        if self.next:
            return str(self.x) + " " + self.next.__str__()
        else:
            return str(self.x)

def i_reverseList(head):

    prev = None

    while head:
        head_node = head.next
        head.next = prev
        prev = head
        head = head_node

    return prev

def r_reverseList(head):
    if (not head or not head.next):
        return head

    reverse_list = r_reverseList(head.next)
    head.next.next = head
    head.next = None

    return reverse_list

l1 = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(5)))))
print(l1)
print(r_reverseList(l1))
