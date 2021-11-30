from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # use DP
        H, W = len(grid), len(grid[0])
        dp = [[-1 for _ in range(W)] for _ in range(H)]
        dp[0][0] = grid[0][0]
        for i in range(H):
            for j in range(W):
                if dp[i][j] == -1:
                    top = float('inf') if i-1 < 0 else dp[i-1][j]
                    left = float('inf') if j-1 < 0 else dp[i][j-1]
                    dp[i][j] = min(top, left) + grid[i][j]
        return dp[-1][-1]
