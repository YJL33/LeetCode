from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dfs+pruning (?)
        # dp, start from top-left
        m, n = len(grid), len(grid[0])
        dp = [[ float('inf') for _ in range(n) ] for _ in range(m)]
        dp[0][0] = grid[0][0]

        # craft first row
        for j in range(1,n):
            dp[0][j] = grid[0][j] + dp[0][j-1]

        # craft first col
        for i in range(1,m):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j])+grid[i][j]
        
        # print('dp:', dp)
        return dp[-1][-1]

print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(Solution().minPathSum([[1,2,3],[4,5,6]]))