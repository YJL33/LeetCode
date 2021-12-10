# 1000000007
class Solution:
    def numTilings(self, n: int) -> int:
        # use DP(?)
        # 2*d[n-1]+dp[n-3]
        if n == 0: return 0
        dp = [1,1,2,5]
        if n <= 3: return dp[n]
        x = 3
        while x < n:
            tmp = 2*dp[-1]+dp[0]
            dp = [dp[-2],dp[-1],tmp]
            x += 1
        return dp[-1]%1000000007

print(Solution().numTilings(5))
print(Solution().numTilings(10))
print(Solution().numTilings(15))