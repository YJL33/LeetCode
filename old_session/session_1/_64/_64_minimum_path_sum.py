"""
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return None
        m = len(grid[0])
        res = [0] + [float('inf') for i in xrange(m-1)]
        for row in grid:
            for j in xrange(m):
                if j == 0:
                    res[j] += row[j]
                else:
                    res[j] = row[j] + min(res[j], res[j-1])
        return res[-1]