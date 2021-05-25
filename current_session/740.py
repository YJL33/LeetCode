"""
740
"""
from typing import List
import collections
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnts = collections.Counter(nums)
        dp = [0,0]          # dp[i] = (max points of pick up i, max points of NOT pick up i)
        prev = None
        ns = sorted(cnts.keys())
        for n in ns:
            a = dp[1]+n*cnts[n]
            if prev and n-prev != 1:             # we can pickup x anyway
                a = max(dp[0]+n*cnts[n], a)
            b = max(dp)
            prev = n
            dp = [a, b]
        return max(dp)

print(Solution().deleteAndEarn([3,4,2]))
print(Solution().deleteAndEarn([2,2,3,3,3,4,4,4,4,4,4,4,4,5,6,6,7,8,10,12,14]))
