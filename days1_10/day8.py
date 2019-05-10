'''
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def unival(node):
    return helper(node, node.val)

def helper(node, val):
    if not node:
        return True
    if node.val == val:
        return helper(node.left, val) and helper(node.right, val)
    return False

def traverse(node):
    if not node:
        return 0
    num = traverse(node.left) + traverse(node.right)
    if unival(node):
        num += 1
    return num


node1 = Node('0', Node('1'), Node('0', Node('1', Node('1'), Node('1')), Node('0')))
node2 = Node('0', Node('1'), Node('1'))
node3 = Node('0', Node('0', Node('0'), Node('0')), Node('0'))
node4 = Node('1')

print(traverse(node1))
print(traverse(node2))
print(traverse(node3))
print(traverse(node4))
