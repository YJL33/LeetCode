class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # dp bottom-up
        # time complexity: O(steps*min(steps, arrLen))
        if arrLen == 1: return 1
        if steps == 1: return 1
        
        # initila state of dp
        # note that we can ignore those too far away from origin
        dp = [[0 for _ in range(min(steps,arrLen))] for _ in range(steps+1)]
        dp[1][0] = 1
        dp[1][1] = 1
        for step in range(2, steps+1):
            dp[step][0] = dp[step-1][0]+dp[step-1][1]
            dp[step][-1] = dp[step-1][-1]+dp[step-1][-2]
            for j in range(1, len(dp[0])-1):
                dp[step][j] += dp[step-1][j]+dp[step-1][j-1]+dp[step-1][j+1]

        return dp[steps][0]%1000000007
