class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]      # dp[i][j] = solution of n=i, k=j
        
        # dp[i][j] = dp[i-1][j]*j + dp[i-1][j-1]
        for i in range(k+1):
            dp[i][i] = 1

        for j in range(1, k+1):
            for i in range(j+1, n+1):
                dp[i][j] = (dp[i-1][j]*j + dp[i-1][j-1])%1000000007
        return dp[-1][-1]