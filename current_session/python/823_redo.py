from typing import List
class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        dp = {}
        for a in A: dp[a] = 1       # base

        A.sort()

        for i in range(len(A)):
            subSum = 0
            for j in range(i+1):
                a, b = A[i], A[j]
                if a%b == 0 and a/b in dp:
                    subSum += dp[b]*dp[a/b]
            dp[a] += subSum
        return sum(dp.values()) % (10**9+7)

print(Solution().numFactoredBinaryTrees([18,3,6,2]))