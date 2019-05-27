'''
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.
'''

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0;
        temp = 0;

        for i in range(31, -1, -1):
            if (temp + (divisor << i) <= dividend):
                temp += divisor << i;
                quotient |= 1 << i;

        if sign*quotient < -2**31 or sign*quotient > 2**31 - 1:
            return 2**31 - 1
        else:
            return sign * quotient;

#Top 99.26% runtime
