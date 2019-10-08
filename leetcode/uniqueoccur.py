'''
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.



Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
'''

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        d = {}

        for el in arr:
            if el in d:
                d[el] += 1
            else:
                d[el] = 1


        dv = d.values()
        for v in dv:
            if not dv.count(v) == 1:
                return False
        return True

# Top 96.22% runtime
