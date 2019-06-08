'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if s == "":
            return True

        if len(s) % 2 == 1:
            return False
        else:
            popped = [s[0]]
            for c in s[1:]:
                if (c == ")" and popped[-1] == "(") or (c == "}" and popped[-1] == "{") or (c == "]" and popped[-1] == "["):
                    popped.pop()
                else:
                    popped.append(c)

            if popped:
                return False
            else:
                return True

#Top 91.81% runtime
