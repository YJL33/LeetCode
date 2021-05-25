"""
63. Unique Paths II

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids.
How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,

There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

The total number of unique paths is 2.

Note: m and n will be at most 100.
"""
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [0 for x in xrange(n)]         # ways to arrive this point
        dp[0] = 1
        
        for i in xrange(m):
            for j in xrange(n):
                if obstacleGrid[i][j]:
                    dp[j] = 0               # if obstacle: no way
                elif j > 0:
                    dp[j] += dp[j-1]        # top + left

        return dp[-1]