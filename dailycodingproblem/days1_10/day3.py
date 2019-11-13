'''
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    serial = [node.val]
    if node.left is None:
        serial.append('-')
    else:
        serial.extend(serialize(node.left))
    if node.right is None:
        serial.append('-')
    else:
        serial.extend(serialize(node.right))
    return serial

def deserialize(string):
    if string[0] == '-':
        return None

    value = string[0]
    print(string)
    left = deserialize(string[1:])
    right = deserialize(string[2:])
    return Node(value, left, right)

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
