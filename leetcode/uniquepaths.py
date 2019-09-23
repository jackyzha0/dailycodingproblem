class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        mat = [[1 for _ in range(n)] for _ in range(m)]
        for c in range(1, n):
            for r in range(1, m):
                mat[r][c] = mat[r][c - 1] + mat[r - 1][c]

        return mat[m-1][n-1]

# Top 99.06% runtime
