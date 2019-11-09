# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False

        queue = [root]

        while queue:
            v = queue.pop(0)
            if not v.val == root.val:
                return False
            if v.left:
                queue.append(v.left)
            if v.right:
                queue.append(v.right)

        return True
