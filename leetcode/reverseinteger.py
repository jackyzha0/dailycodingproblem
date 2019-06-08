'''
Given a 32-bit signed integer, reverse digits of an integer.
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign = -1 if x < 0 else 1

        i = int(str(abs(x))[::-1])

        if i > (2**31 - 1):
            return 0
        else:
            return  i * sign

#Top 98.4% runtime
