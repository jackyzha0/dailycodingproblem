class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def bfs(_y, _x):
            q = [(_y,_x)]
            while q:
                (y,x) = q.pop()
                grid[y][x] = "0"

                if not y == 0 and grid[y-1][x] == "1":
                    q.append((y-1, x))
                if not y == len(grid)-1 and grid[y+1][x] == "1":
                    q.append((y+1, x))
                if not x == len(grid[0])-1 and grid[y][x+1] == "1":
                    q.append((y,x+1))
                if not x == 0 and grid[y][x-1] == "1":
                    q.append((y,x-1))

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])): #find land
                if grid[i][j] == "1":
                    bfs(i,j)
                    res += 1
        return res

# Top 99.61% runtime
