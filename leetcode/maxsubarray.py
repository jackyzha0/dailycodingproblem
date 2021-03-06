'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return []

        if len(nums) == 1:
            return nums[0]

        largest = current = -999999999999

        for n in nums:
            current = max(n, n + current)
            largest = max(largest, current)

        return largest

# Top 98.97% runtime
