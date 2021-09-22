# DP
# gradually increase from 1 to sqrt(n)
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf') for _ in range(n+1)]
        for i in range(1, int(pow(n, 0.5))+1):
            dp[i*i] = 1

        for i in range(2, n+1):
            if dp[i] == float('inf'):
                for j in range(int(i**0.5)+1):
                    dp[i] = dp[i-j**2]+1 if dp[i-j**2]+1 < dp[i] else dp[i]

        return dp[n]

print(Solution().numSquares(13))
print(Solution().numSquares(12))
print(Solution().numSquares(9))