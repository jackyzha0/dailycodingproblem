'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for x in range(len(nums)):
            try:
                targ_ind = nums.index(target - nums[x])
                if x != targ_ind:
                    return [x, targ_ind]
            except:
                pass

# Top 43.5% runtime
