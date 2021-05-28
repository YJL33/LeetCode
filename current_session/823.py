"""
823
"""
from typing import List
class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        dp = {}
        for a in sorted(A):
            subSum = 0
            for b in dp:
                if a%b == 0:
                    subSum += dp[b]*dp.get(a/b, 0)
            dp[a] = subSum + 1
            # print('dp:',dp)
        return sum(dp.values()) % (10**9 + 7)

print(Solution().numFactoredBinaryTrees([2,4]))
print(Solution().numFactoredBinaryTrees([2,4,5,10]))
print(Solution().numFactoredBinaryTrees([2,4,16,40]))