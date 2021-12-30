from typing import List
import collections
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # use DP
        # dp = [max point of delete this, max point of don't delete this]
        # get all unique Ns, sort and check each of them
        # if n == prevN+1: dp = [ dp[1]+n*cnt[n], max(dp)]
        # else: 
        numCount = collections.Counter(nums)
        uniqueN = [n for n in numCount.keys()]
        uniqueN.sort()
        dp = [0,0]
        prevN = None
        for n in uniqueN:
            if prevN and n == prevN+1:
                dp = [dp[1]+n*numCount[n], max(dp)]
            else:
                dp = [max(dp)+n*numCount[n], max(dp)]   # use either will be fine
            prevN = n
        return max(dp)

print(Solution().deleteAndEarn([3,4,2]))
print(Solution().deleteAndEarn([2,2,3,3,3,4]))
print(Solution().deleteAndEarn([2,2,3,3,3,4,4,4,4,4,4,4,4,5,6,6,7,8,10,12,14]))

