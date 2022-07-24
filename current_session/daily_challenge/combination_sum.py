from functools import lru_cache
from typing import List
import collections
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # dfs
        # start from each element
        # only check the element after it
        candidates.sort()
        if target < candidates[0]: return []

        self.res = []
        N = len(candidates)
        def dfs(i, target, prev=[]):
            # print('given:', i, target, prev)
            if target < 0:
                return
            if target == 0:
                self.res.append(prev)
                return
            for j in range(i, N):
                dfs(j, target-candidates[j], prev+[candidates[j]])
            return
        
        dfs(0, target)
        return self.res

    def combinationSum_memoization(self, candidates: List[int], target: int) -> List[List[int]]:
        # dp top down
        N = len(candidates)

        @lru_cache
        # return a list of combinations that has sum == x
        def dp(x, start):
            if x == 0: return [[]]
            res = []
            for i in range(start, N):
                c = candidates[i]
                if x-c >= 0:
                    comp = dp(x-c, i)
                    if comp:
                        for y in comp:
                            res.append(y+[c])
            return res

        return dp(target, 0)

    def combinationSum_tablization(self, candidates: List[int], target: int) -> List[List[int]]:
        # dp bottom up
        dp = collections.defaultdict(list)
        dp[0] = [[]]

        for c in candidates:
            for t in range(1, target+1):
                if t-c >= 0 and dp[t-c]:
                    for x in dp[t-c]:
                        dp[t].append([c]+x)
        
        return dp[target]

print(Solution().combinationSum_memoization([2],1))
print(Solution().combinationSum_memoization([2,3,5],8))
print(Solution().combinationSum_memoization([2,3,6,7],7))