"""
https://leetcode.com/problems/perfect-squares/
"""
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp
        # for all p^2 <= i,  dp[i] = dp[i-p^2] + 1
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        # p = int(n**0.5)+1
        for i in range(n+1):
            m = int(n**0.5)+1
            for j in range(m):
                dp[i] = min(dp[i], dp[i-j**2]+1)

        return dp[n]

    # exists an mathematical way

print(Solution().numSquares(12), '4,4,4')
print(Solution().numSquares(13), '9,4')
print(Solution().numSquares(43), '25,9,9')
