"""
63
"""
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        H, W = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for i in range(W)] for j in range(H)]
        i, j = H-1, W-1
        while i >= 0 and obstacleGrid[i][-1] != 1:
            dp[i][-1] = 1
            i -= 1
        while j >= 0 and obstacleGrid[-1][j] != 1:
            dp[-1][j] = 1
            j -= 1
        
        for i in range(H-2, -1, -1):
            for j in range(W-2, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        
        return dp[0][0]

print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(Solution().uniquePathsWithObstacles([[0,1],[0,0]]))
