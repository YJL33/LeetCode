from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # use dp
        # dp[i] = solution at i (including i)
        # track localmin, localmax, update globalmax
        globalmax, localmin, localmax = nums[0], nums[0], nums[0]
        for i in range(1,len(nums)):
            globalmax = max(globalmax, nums[i]*localmin, nums[i]*localmax, nums[i])
            localmin, localmax = min(nums[i], localmin*nums[i], localmax*nums[i]), max(nums[i], localmin*nums[i], localmax*nums[i])
            # print(localmin, localmax, globalmax)
        return globalmax