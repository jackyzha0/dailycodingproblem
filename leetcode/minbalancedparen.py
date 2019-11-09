class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        res = 0

        for p in S:
            if p == "(":
                stack.append(p)
            else:
                if stack:
                    v = stack.pop()
                    if not v == "(":
                        res += 1
                else:
                    res += 1
        return res + len(stack)
