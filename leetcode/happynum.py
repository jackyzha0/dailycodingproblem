class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n == 58:
            return False

        s = 0
        while (n):
            s += (n % 10)**2
            n = n / 10
        return self.isHappy(s)
