# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

         # if not leaf and left exists
        if root.left:
             root.left = self.pruneTree(root.left)
        if root.right:
             root.right = self.pruneTree(root.right)

         # check if leaf
        if not root.left and not root.right:
            if root.val == 0:
                return None

        return root
