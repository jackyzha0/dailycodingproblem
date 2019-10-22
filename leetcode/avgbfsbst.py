# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        if not root:
            return []

        queue = [root, "end"]
        row = []
        res = []

        while queue:
            val = queue.pop(0)

            if val == "end":
                if len(row) > 0:
                    res.append(float(sum(row))/float(len(row)))
                    row = []
                    queue.append("end")
            else:
                row.append(val.val)
                if val.left:
                    queue.append(val.left)
                if val.right:
                    queue.append(val.right)

        return res
