"""
1335
"""
import collections
class Solution:
    def minDifficulty(self, A, d):
        if len(A) < d:
            return -1
        if len(A) == d:
            return sum(A)
        if d == 1:
            return max(A)

        # use dp
        # dp[d][i]: the answer of starting from that index i, d days left
        # dp[0] is useless
        # e.g.
        # dp[6][0] = min(inf, A[0]+dp[5][1])
        
        # fill dp
        L = len(A)
        dp = [[float('inf') for _ in range(L)]+[0] for _ in range(d+1)]

        for dd in range(1,d+1):
            # maintain maxD
            for i in range(L-dd+1):
                maxD = 0
                localAns = float('inf')
                for j in range(i, L-dd+1):
                    maxD = max(A[j], maxD)
                    # print('dd, i, j, maxD, dp[dd-1][j+1], LocalAns: ', dd, i, j, maxD, dp[dd-1][j+1], localAns)
                    localAns = min(localAns, maxD+dp[dd-1][j+1])
                dp[dd][i] = localAns
                # print('=== stop updating dp[', dd, '][', i, ']', '===>', dp[dd][i])
        # print(dp)
        return dp[d][0] if dp[d][0] < float('inf') else -1
                
# print(Solution().minDifficulty([9,9,9], 4))
# print(Solution().minDifficulty([9,9,9], 3))
# print(Solution().minDifficulty([6,5,4,3,2,1], 2))
print(Solution().minDifficulty([22,222,11,111,33,333,44,444], 7))