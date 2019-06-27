'''
Given the head of a singly linked list, reverse it in-place.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def day73(head):
    prev = None
    node = head

    while curr:
        _ = node.next
        node.next = prev
        prev = node
        node = _

    return prev
