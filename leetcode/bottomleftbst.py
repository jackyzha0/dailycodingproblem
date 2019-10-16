# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # bfs

        queue = []
        queue.append(root)

        while len(queue) > 0:
            node = queue.pop(0)

            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val

# Top 93.55% runtime
