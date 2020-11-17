"""
https://leetcode.com/problems/minimum-path-sum/
"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        dp = [[0 for _ in grid[0]] for _ in grid]
        dp[0][0] = grid[0][0]

        # 1st row
        for j in range(1,len(grid[0])):
            dp[0][j] = grid[0][j]+dp[0][j-1]
        # 1st col
        for i in range(1,len(grid)):
            dp[i][0] = grid[i][0]+dp[i-1][0]
        # rest
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i-1][j])
        # print(dp)

        return dp[-1][-1]

print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))