class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid:
            return 0

        overall = 0

        def dfs(y, x):
            res = 1
            grid[y][x] = 0
            if not y == 0 and grid[y-1][x] == 1:
                res += dfs(y-1, x)
            if not y == len(grid)-1 and grid[y+1][x] == 1:
                res += dfs(y+1, x)
            if not x == len(grid[0])-1 and grid[y][x+1] == 1:
                res += dfs(y,x+1)
            if not x == 0 and grid[y][x-1] == 1:
                res += dfs(y,x-1)
            return res

        for i in range(len(grid)):
            for j in range(len(grid[0])): #find land
                if grid[i][j]:
                    overall = max(overall, dfs(i,j))

        return overall

# Top 94.62% runtime
