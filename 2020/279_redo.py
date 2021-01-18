"""
279
"""
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp
        # 1,4,9,16....
        # dp[n] = min(dp[n-a^2] for all a)
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0

        # put sqrt first
        i = 1
        while i**2 <= n:
            dp[i**2] = 1
            i += 1

        # fill the array
        for j in range(2,n+1):
            if dp[j] == float('inf'):
                sqrts = range(int(j**0.5)+1)
                # print(j, sqrts)
                dp[j] = min(dp[j-s**2]+1 for s in sqrts)

        # print dp
        return dp[-1]

print(Solution().numSquares(12), '4,4,4')
print(Solution().numSquares(13), '9,4')
print(Solution().numSquares(43), '25,9,9')

