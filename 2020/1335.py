"""
1335
"""
import functools
class Solution:
    def minDifficulty(self, A, d):
        n = len(A)
        if n < d: return -1

        @functools.lru_cache
        def dfs(i, d):
            if d == 1:
                return max(A[i:])
            res, maxd = float('inf'), 0
            for j in range(i, n-d+1):
                maxd = max(maxd, A[j])
                res = min(res, maxd + dfs(j+1, d-1))
            return res
        return dfs(0, d)
                
# print(Solution().minDifficulty([9,9,9], 4))
# print(Solution().minDifficulty([9,9,9], 3))
# print(Solution().minDifficulty([6,5,4,3,2,1], 2))
print(Solution().minDifficulty([11,111,22,222,33,333,44,444], 6))