'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

class Solution(object):
    def prefIn(self, pref, strs):
        l = len(pref)
        for x in strs:
            if not pref in x[:l]:
                return False
        return True

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        try:
            a = [len(x) for x in strs]
            i = a.index(min(a))

            prefix = strs[i]

            while not self.prefIn(prefix, strs):
                prefix = prefix[:-1]

            return prefix

        except:
            return ""

#Top 99.53% runtime
