# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        d = {}

        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        return [x[0] for x in sorted(d.items(), reverse = True, key=lambda x: x[1])[:k]]
