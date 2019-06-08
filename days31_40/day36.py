'''
Given the root to a binary search tree, find the second largest node in the tree.
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def findSecondLargest(root):
    largest = root.val
    second = 0
    while root is not None:
        if root.val >= largest:
            largest, second = root.val, largest
        elif root.val >= second:
            second = root.val

        if root.right:
            root = root.right
        else:
            root = root.left
    return second
