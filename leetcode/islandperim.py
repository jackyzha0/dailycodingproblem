# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
#
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
#
# The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    bot = y == len(grid)-1
                    top = y == 0
                    left = x == 0
                    right = x == len(grid[0])-1
                    if top or grid[y-1][x] == 0:
                        res += 1
                    if bot or grid[y+1][x] == 0:
                        res += 1
                    if left or grid[y][x-1] == 0:
                        res += 1
                    if right or grid[y][x+1] == 0:
                        res += 1

        return res
