# Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.
#
#     a
#    / \
#   b   c
#  /
# d

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def retDeepest(t):
    queue = [t]
    deepest = None
    while queue:
        val = queue.pop(0)
        deepest = val.val

        if val.left:
            queue.append(val.left)

        if val.right:
            queue.append(val.right)

    return deepest

t = TreeNode("a")
t.right = TreeNode("c")
t.left = TreeNode("b")
t.left.left = TreeNode("d")

assert retDeepest(t) == "d"
