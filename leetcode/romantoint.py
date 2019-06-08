'''
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        val = 0

        map = {"I": 1,
               "V": 5,
               "X": 10,
               "L": 50,
               "C": 100,
               "D": 500,
               "M": 1000}

        string = s

        while len(string) > 0:
            if len(string) >= 2 and map[string[0]] < map[string[1]]:
                val += (map[string[1]] - map[string[0]])
                string = string[2:]
            else:
                val += map[string[0]]
                string = string[1:]

        return val

#Top 98.95% runtime
