# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        queue = [root, "end_layer"]
        cur_sum = 0
        sums = []
        while queue:
            val = queue.pop(0)
            if val == "end_layer":
                sums.append(cur_sum)
                cur_sum = 0
                if queue:
                    queue.append("end_layer")
            else:
                cur_sum += val.val
                if val.left:
                    queue.append(val.left)
                if val.right:
                    queue.append(val.right)
        return sums.index(max(sums)) + 1
