from typing import List
import collections
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = collections.defaultdict(list)
        dp[0] = [[]]
        # for c in candidates:
        #     dp[c].append([c])

        for c in candidates:
            for t in range(1, target+1):
                if t-c >= 0 and dp[t-c]:
                    for x in dp[t-c]:
                        dp[t].append([c]+x)
        
        return dp[target]

print(Solution().combinationSum([2,3,6,7],7))
print(Solution().combinationSum([2,3,5],8))
print(Solution().combinationSum([2],1))
print(Solution().combinationSum([1],1))