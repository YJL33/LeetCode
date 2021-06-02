"""
740
"""
from typing import List
import collections
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # DP
        # either delete that number or not
        cnt = collections.Counter(nums)
        dp = [0,0]
        ns = [k for k in cnt.keys()]
        ns.sort()
        for i in range(len(ns)):
            # dp[n]: max val of delete n / don't delete n
            n = ns[i]
            if i > 0 and n == ns[i-1]+1:
                dp = [cnt[n]*n+dp[1], max(dp)]
            else:
                dp = [cnt[n]*n+max(dp), max(dp)]
        return max(dp)

print(Solution().deleteAndEarn([2,2,3,3,3,4]))
# print(Solution().deleteAndEarn([3,4,2]))
# print(Solution().deleteAndEarn([2,2,3,3,3,4,4,4,4,4,4,4,4,5,6,6,7,8,10,12,14]))

