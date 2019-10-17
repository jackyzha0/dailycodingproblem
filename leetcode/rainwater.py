# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        highest = -1
        h_i = -1
        for i, h in enumerate(height):
            if h > highest:
                h_i, highest = i, h

        # left subproblem
        lowest = -1
        for h in height[:h_i]:
            if h > lowest:
                lowest = h

            water += lowest - h

        # right subproblem
        lowest = -1
        for h in height[h_i:][::-1]:
            if h > lowest:
                lowest = h

            water += lowest - h

        return water

# Top 75.62% runtime
