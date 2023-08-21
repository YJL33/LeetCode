from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # use DP
        # where dp[i] is the max consecutive length while we have i remaining flips
        # go through the given nums
        # time complexity: O(kN)

        # edge case
        if len(nums)-sum(nums) <= k: return len(nums)
        
        # use sliding window
        # track zeros within the window
        # note that the window size is expanded while go through the array (never decrease)
        # time complexity: O(N)
        l = 0
        for r in range(len(nums)):
            k -= 1-nums[r]
            # as long as k<0, the window size will stop increasing
            # say current window size = x
            # it will keep tracking nums[r-x:r+1] until k == 0
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
        return r-l+1

print(Solution().longestOnes([1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,1,1,1,1,0,0,1,1,1,0,0,1,1,0,0,1,1,1,0,1,0,0,1,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,1,1,1,0,0,0,0,1,0,0,0,1,1,0,1,0,0,0,0,1,0,0,1,1,1,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,1,1,0,1,0,0,0,0,0,0,1,1,1,0,0,0,1,0,1,1,0,1,1,1,1,1,1,0,1,1,1,0,0,1,0,1,0,1,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,1,0,0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,1,0,1,0,1,0,0,0,1,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,1,1,0,0,1,1,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,1,0,1,1,1,1,0,0,0,0,1,0,1,0,0,1,1,1,0,1,1,1,1,0,1,1,0,0,0,1,0,1,1,0,1,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1,1,0,1,1,0,1,1,1,0,0,1,0,1,1,1,0,0,0,1,0,0,0,1,1,1,1,0,0,0,1,1,0,0,1,1,1,0,0,1,0,1,0,0,0,0,1,1,1,0,0,1,1,0,0,1,0,0,0,1,1,1,0,0,0,0,1,0,1,0,0,1,0,0,1,1,0,0,1,0,1,0,1,1,1,1,0,0,1,0,0,1,1,1,0,1,1,1,0,0,0,1,0,0,1,0,0,1,1,0,1,1,1,1,0,1,0,0,0,1,1,0,1,1,1,0,0,0,1,1,0,0,0,1,0,0,0,1,0,1,1,1,1,0,0,0,0,1,1,1,0,0,1,1,0,0,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,0,1,1,1,1,0,0,0,1,1,0,0,1,1,1,1,1,0,1,0,0,0,1,1,1,1,1,0,1,1,1,1,0,0,1,1,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,1,0,0,1,0,0,1,1,0,1,1,0,1,1,0,0,1,1,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,0,1,0,0,1,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,1,0,0,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,0,1,1,0,0,1,1,1,1,0,1,1,0,1,1,0,1,0,1,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,1,0,1,0,1,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,0,0,0,1,1,0,0,1,1,0,0,1,0,1,1,1,0,1,1,0,0,0,1,0,0,0,1,0,1,1,0,1,1,1,1,0,1,0,1,1,0,0,1,1,1,1,0,1,0,0,0,1,1,0,1,0,0,1,0,1,1,0,0,1,1,0,0,0,0,1,1,0,0,0,1,0,0,1,0,1,0,0,1,1,0,0,1,1,1,1,0,0,0,1,1,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,0,0,0,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,1,1,1,1,1,0,1,0,0,0,1,0,0,1,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,0,1,1,0,1,1,1,0,1,0,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,0,1,0,0,1,1,0,1,1,1,0,1,0,0,0,0,1,0,0,1,0,1,0,1,1,0,1,0,0,1,0,1,0,1,1,1,0,1,1,1,0,0,1,0,0,1,0,0,1,1,1,0,1,1,0,0,0,1,0,0,1,1,0,0,0,0,0,0,1,1,1,0,1,0,1,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,1,0,0,1,0,1,1,1,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,0,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,0,1,0,1,1,0,1,1,0,0,1,1,0,0,0,1,0,1,0,0,1,0,0,1,0,1,1,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,1,1,0,1,1,0,0,0,1,0,1,1,0,1,1,0,0,1,1,1,1,1,0,0,0,0,1,0,1,0,1,1,0,1,0,1,0,0,0,0,0,0,1,1,1,0,1,0,1,1,1,0,0,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,0,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1,0,0,1,0,0,0,1,1,0,1,1,1,1,0,1,1,0,1,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,1,0,1,1,1,0,0,0,0,1,0,1,1,1,0,1,1,0,1,0,1,1,0,1,1,1,1,0,1,1,1,0,0,1,1,0,0,1,1,0,1,1,0,0,1,1,0,1,0,1,0,1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,1,0,0,0,0,1,1,0,1,1,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,0,0,1,1,0,0,0,0,1,0,0,1,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,1,0,0,1,0,0,0,1,1,1,1,0,0,1,0,0,0,1,0,0,1,1,0,1,0,1,1,0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,1,1,0,1,1,0,1,0,1,0,0,1,1,0,1,0,0,1,1,0,0,0,0,1,1,1,1,0,1,0,0,1,1,0,1,0,1,1,1,1,1,1,1,0,0,0,1,0,0,1,1,0,1,1,1,1,1,1,0,0,0,0,0,1,0,1,0,0,0,1,1,1,0,1,1,0,0,1,0,0,1,0,0,0,1,1,1,0,1,1,0,0,0,1,0,0,0,0,1,0,1,1,0,0,0,1,0,0,1,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,1,0,0,1,1,0,0,0,0,1,0,0,1,1,1,1,0,0,0,0,1,0,1,1,0,1,1,1,1,0,1,0,0,1,1,1,0,0,0,1,1,1,0,0,1,0,0,0,1,1,1,0,0,0,1,0,0,1,1,1,1,1,0,1,1,0,0,0,1,1,0,0,1,1,0,1,1,0,0,1,0,1,1,1,0,1,1,0,1,0,1,1,0,1,1,0,0,1,1,1,1,0,0,0,0,1,0,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,0,0,1,1,1,1,0,1,1,1,0,1,0,1,1,0,1,1,1,1,0,1,1,1,1,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,1,1,0,1,1,1,1,0,0,0,1,0,0,1,1,0,0,0,0,1,0,1,0,1,1,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,1,0,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,1,0,1,1,1,1,0,0,1,1,1,0,1,0,0,0,0,1,1,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1,1,1,1,0,0,1,0,1,1,1,0,0,1,1,0,0,0,1,1,1,0,0,1,1,1,0,1,1,0,0,1,1,0,1,1,0,0,1,1,0,0,1,1,1,0,0,0,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0,0,1,0,1,1,0,1,1,0,0,0,0,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,0,1,0,1,1,0,1,0,0,1,1,0,1,1,0,1,0,0,0,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1,0,1,0,1,1,0,0,0,0,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,1,0,0,1,1,1,1,1,0,0,1,0,1,1,0,1,1,0,0,1,1,0,1,1,0,0,1,1,0,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,1,1,0,1,0,0,1,0,1,0,0,0,0,0,0,1,0,1,1,0,1,1,0,0,0,0,1,1,0,1,0,1,0,0,1,0,1,1,1,0,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,0,1,1,0,1,0,0,0,0,1,1,0,1,1,1,0,0,0,1,0,1,0,0,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,0,0,0,0,1,1,1,0,0,0,1,1,0,1,1,0,1,0,1,1,0,0,0,0,1,1,1,1,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,0,1,1,1,1,0,0,1,0,0,0,0,0,1,0,0,1,0,1,1,0,0,0,0,1,1,1,1,0,1,0,0,1,0,0,0,0,0,1,0,1,1,1,1,0,1,0,1,0,0,0,0,0,0,0,1,1,0,0,1,1,1,0,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1,0,1,1,1,1,1,0,1,0,0,0,0,0,1,1,1,0,1,0,0,1,0,1,1,0,1,1,1,0,0,0,1,1,1,0,1,0,0,0,0,1,0,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,0,0,1,1,1,1,0,0,1,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,1,1,0,1,1,1,0,1,1,1,0,1,0,0,1,1,0,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,1,0,0,1,1,1,0,1,1,1,0,1,1,0,1,0,0,1,1,1,1,0,1,1,1,0,0,1,0,0,0,0,1,1,1,1,1,0,1,0,0,0,0,1,0,0,1,1,0,1,0,0,0,1,1,0,0,1,1,0,1,1,0,0,0,1,1,0,1,0,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,1,1,0,1,1,1,1,1,0,0,1,0,1,1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,0,0,1,1,0,1,1,0,0,0,0,1,1,1,0,0,0,1,0,0,1,1,1,0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,0,0,0,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,0,0,0,0,0,1,0,1,1,0,1,1,0,1,1,1,1,1,0,0,0,0,1,1,0,1,1,1,0,0,0,0,0,1,0,1,0,1,1,1,0,1,1,0,1,0,1,1,1,0,1,1,0,0,1,1,0,1,1,0,1,1,1,0,0,0,1,0,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,0,0,0,1,1,0,0,0,0,1,0,1,0,1,0,1,1,1,0,1,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,0,1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,0,1,0,0,1,0,1,0,1,1,0,0,1,0,1,1,0,1,1,0,1,1,0,0,1,0,1,1,1,1,1,0,1,1,1,0,1,0,0,0,1,1,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,0,0,1,1,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,1,0,1,0,0,1,1,0,0,1,0,1,0,1,0,0,0,1,1,1,1,0,1,1,0,0,1,1,0,0,1,1,1,0,0,1,0,0,1,0,0,1,0,1,1,0,0,0,0,0,1,0,0,0,1,0,0,1,1,1,0,1,1,1,1,0,1,0,1,0,1,1,0,1,1,1,0,0,0,1,0,0,1,1,1,0,0,0,0,1,1,0,1,0,0,0,0,0,1,0,1,0,1,1,0,1,1,0,1,1,1,0,0,0,0,1,0,1,0,0,1,1,0,0,1,1,1,1,1,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0,0,0,1,1,0,1,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1,1,1,1,0,0,1,1,1,1,1,0,1,1,0,0,1,1,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,1,0,1,1,0,1,1,0,0,0,1,1,1,1,1,1,0,1,0,1,1,0,0,1,0,0,0,1,0,0,1,0,0,1,1,0,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,0,0,1,1,0,1,0,0,1,1,0,1,1,0,0,0,1,1,0,0,0,1,0,0,1,1,0,1,1,1,0,0,1,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,0,0,0,1,0,0,1,1,1,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0,0,0,1,1,0,0,1,1,1,0,1,1,0,0,1,1,0,0,1,1,1,1,1,0,1,1,1,1,0,0,1,0,0,1,0,0,1,1,1,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,0,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,0,0,1,0,1,1,0,0,1,0,0,0,1,1,0,1,1,0,0,0,0,0,0,1,1,0,1,0,0,0,1,1,1,1,0,0,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,1,1,0,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0,0,0,1,1,0,1,0,1,1,1,1,0,0,1,1,1,0,0,1,1,0,1,0,0,1,0,0,1,0,0,0,1,1,0,1,0,1,1,0,0,1,0,1,1,0,0,0,1,0,0,0,1,1,1,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,1,0,1,1,0,1,0,0,1,1,1,1,1,0,1,0,1,1,0,1,0,0,1,1,1,0,0,1,0,0,1,1,0,0,1,0,0,1,0,1,0,1,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,0,1,0,0,0,1,0,1,1,1,0,0,1,1,1,0,0,0,0,1,1,0,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,0,1,1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,1,0,0,0,1,1,0,0,0,1,1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,0,1,0,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0,0,1,1,0,0,1,0,1,1,0,1,0,1,1,0,0,1,0,0,0,1,1,0,0,0,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,0,1,0,1,0,1,0,1,1,1,0,1,1,0,1,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,1,1,1,0,0,0,1,0,1,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,0,1,1,1,1,0,0,0,1,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,1,0,1,1,0,1,1,1,0,0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,0,0,1,0,0,0,1,1,1,1,0,1,0,0,1,0,1,1,0,0,1,1,1,0,1,0,1,1,1,0,1,1,0,0,0,1,0,0,1,0,1,0,1,0,0,0,1,0,1,1,0,1,0,1,0,0,1,1,0,0,0,0,1,1,0,1,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,1,0,1,0,1,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0,1,1,1,1,0,1,1,0,0,0,0,0,1,0,1,1,1,0,0,1,1,0,1,0,1,0,1,0,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,1,0,0,1,0,1,0,0,0,1,1,0,1,1,0,0,1,0,1,0,0,1,0,0,0,1,1,1,0,0,1,0,1,1,1,0,0,0,1,1,0,0,0,1,1,0,0,1,0,0,1,1,0,1,0,1,1,0,0,1,0,1,1,1,1,1,0,0,1,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,0,0,1,1,1,0,0,1,1,0,1,1,0,0,0,0,1,1,0,1,0,0,0,1,1,1,0,1,0,1,1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,1,0,0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,1,0,1,1,1,0,1,0,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,0,1,1,1,0,1,0,1,1,0,1,0,0,1,1,0,1,1,0,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,1,0,0,1,1,1,1,0,1,1,0,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,0,1,1,1,0,1,0,0,1,1,0,0,0,1,0,1,0,1,0,1,1,0,1,1,1,1,0,1,1,0,1,1,1,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,0,1,0,0,1,0,1,0,1,0,1,0,0,1,1,0,1,0,1,0,1,1,1,1,0,1,0,0,0,0,0,1,1,0,1,0,1,0,1,1,1,0,0,0,1,0,0,1,1,0,1,0,0,0,0,0,0,1,1,1,0,1,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,0,1,0,1,0,0,1,0,1,0,1,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0,0,0,1,0,1,1,0,1,1,1,0,0,1,1,1,0,0,1,0,1,0,1,0,0,1,1,1,0,0,1,0,0,1,1,1,1,1,0,0,1,0,1,0,1,0,0,1,1,1,1,1,0,1,0,0,0,0,1,0,0,1,0,1,1,1,0,0,0,1,1,0,1,1,0,0,0,1,1,1,0,1,0,0,0,0,0,1,0,1,1,1,0,1,1,1,1,1,0,0,1,1,0,1,1,0,0,1,0,1,0,1,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,0,0,0,1,0,1,1,0,0,1,0,1,1,1,0,0,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,1,0,0,0,1,1,0,0,1,1,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,0,0,1,1,1,1,0,1,0,0,1,0,1,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,1,1,0,1,1,1,0,0,1,1,0,1,1,0,1,0,1,1,1,1,1,1,1,1,0,1,0,0,0,1,0,1,1,1,1,0,0,0,1,1,1,0,0,1,0,1,0,1,1,0,0,1,1,1,1,0,0,1,0,0,0,0,1,1,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,0,1,1,0,1,0,0,1,0,1,0,1,0,0,1,1,1,1,1,1,0,1,1,0,0,0,1,0,1,0,0,1,1,1,1,1,1,1,1,0,1,0,0,1,0,0,1,1,0,0,1,0,0,1,0,1,1,0,1,1,1,1,0,0,1,0,1,0,1,1,1,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,0,0,0,0,1,1,0,1,1,0,1,1,1,1,0,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,1,0,0,1,1,0,1,0,0,1,0,0,0,1,1,1,0,1,1,0,0,0,0,1,0,1,1,0,1,0,0,0,0,1,0,1,1,1,1,1,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,1,0,0,0,1,0,1,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,1,1,1,1,1,0,1,0,1,1,0,0,0,0,0,0,0,1,0,1,0,1,1,0,1,0,1,1,1,0,0,0,1,0,1,1,0,1,1,0,1,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,1,1,0,1,1,0,1,1,0,1,0,1,0,1,1,1,0,0,0,0,1,1,0,1,0,1,1,1,1,0,1,0,1,1,0,1,1,1,0,0,0,1,0,1,0,1,0,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,0,1,1,1,0,1,0,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1,0,1,1,1,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,1,1,1,1,1,1,0,0,1,0,0,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,0,1,0,0,1,0,1,1,1,1,0,1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,0,0,0,1,0,1,1,0,1,0,0,0,1,0,0,0,0,1,1,1,1,1,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,1,0,0,1,0,1,1,0,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,0,1,1,1,1,0,0,1,0,1,0,1,1,0,1,1,1,1,0,0,0,1,1,0,0,0,1,1,0,1,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0,1,1,0,0,0,0,0,0,1,1,0,1,1,0,1,0,1,0,1,1,1,0,0,1,0,0,1,1,1,1,0,0,0,0,1,1,0,0,0,1,1,0,1,0,1,1,0,0,0,0,1,1,0,1,1,1,1,0,0,0,0,1,0,0,1,0,0,0,1,1,1,0,0,1,1,0,1,1,0,1,1,1,0,0,1,0,0,0,0,0,1,1,0,0,0,1,1,0,1,0,1,0,0,0,0,1,1,1,1,1,1,0,1,1,0,1,0,0,0,1,0,1,0,0,0,0,1,1,1,1,1,1,0,1,0,1,0,0,1,1,0,0,0,1,1,1,0,1,1,1,0,1,1,0,1,0,0,0,1,0,0,1,0,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,1,1,0,1,0,0,1,0,1,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,1,1,1,0,0,0,0,0,1,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,1,1,0,0,1,0,1,0,0,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,0,0,0,1,1,0,0,0,0,1,1,0,0,1,0,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,0,0,0,1,0,0,0,1,0,0,1,1,0,0,1,1,0,0,1,1,0,1,1,0,0,0,0,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,1,0,1,1,0,1,0,0,0,1,1,1,1,1,1,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,1,1,1,1,1,0,0,0,1,0,0,1,0,0,0,1,1,0,1,1,1,0,1,1,1,0,1,0,0,0,0,1,1,1,1,1,1,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,1,1,1,1,1,0,0,1,0,0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,1,1,1,1,0,1,1,0,0,0,0,0,1,0,1,0,0,1,1,0,0,0,0,1,1,1,1,0,0,0,1,0,1,1,0,1,1,0,0,1,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0,0,0,0,1,1,0,1,0,1,0,1,1,1,0,0,0,1,1,1,0,1,1,0,1,0,0,0,1,0,1,1,0,1,1,0,1,1,0,0,1,1,1,0,0,1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,0,0,0,1,1,1,1,1,1,0,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,0,0,1,0,1,1,1,1,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,0,0,1,0,0,0,0,1,0,1,1,0,0,1,0,0,0,0,1,1,1,0,0,1,1,1,0,1,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,1,1,0,0,0,1,0,0,0,0,1,1,0,0,1,0,0,1,1,1,0,1,0,1,0,1,1,0,1,0,1,1,1,1,0,1,0,1,0,0,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,1,1,0,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,0,1,1,0,1,1,0,0,0,0,1,0,0,0,1,1,0,1,0,1,0,0,0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,0,1,1,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,0,0,0,1,1,0,1,1,1,0,1,1,1,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,1,0,0,0,1,1,0,0,0,1,1,0,1,0,0,1,1,0,1,1,0,1,1,0,0,1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,1,0,1,1,1,1,1,0,1,0,1,1,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,1,0,1,1,0,0,1,0,0,1,0,1,0,0,1,1,0,1,0,1,0,1,0,0,0,0,1,1,0,1,0,1,0,1,1,1,0,0,0,1,1,1,0,1,1,1,0,1,0,0,0,1,1,1,0,1,1,0,0,0,0,1,1,1,0,1,0,0,1,0,0,0,0,1,1,1,1,0,0,0,0,1,0,1,0,1,0,0,0,1,1,0,0,0,1,1,1,0,0,0,1,0,0,0,1,0,1,1,0,0,1,0,1,1,0,0,0,0,1,1,0,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,1,0,0,1,0,1,0,0,1,0,0,0,1,0,1,0,1,1,0,1,1,1,0,0,1,0,1,1,1,1,0,1,1,0,1,1,0,0,0,0,0,0,1,1,0,0,1,0,1,0,0,1,1,0,1,0,1,1,1,0,1,1,0,1,1,1,0,1,1,1,1,0,0,0,0,1,0,1,0,1,1,1,1,0,1,1,1,1,0,1,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0,0,0,1,0,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,0,1,0,0,1,0,0,1,1,1,0,1,0,1,0,1,0,1,1,1,0,0,0,0,1,1,0,0,1,0,1,1,1,0,1,0,0,0,1,1,0,0,0,0,0,1,0,0,0,1,1,0,1,0,1,1,0,1,0,1,0,0,1,1,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,1,0,1,0,0,1,0,0,0,1,1,0,1,0,1,0,0,1,0,1,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,0,0,0,0,1,0,0,1,1,1,1,0,0,1,0,0,1,0,1,0,1,1,1,1,0,1,1,0,0,1,0,1,1,0,1,0,1,1,1,0,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,0,1,0,0,1,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,1,0,0,1,0,0,1,1,0,1,1,1,1,1,0,1,0,1,0,0,0,0,0,0,1,0,0,0,1,1,0,1,1,0,0,0,1,1,0,0,1,0,0,1,1,0,1,1,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,1,0,1,0,0,1,0,0,0,1,1,0,0,0,0,0,1,0,1,1,0,0,1,1,0,1,1,1,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,0,0,1,0,0,0,1,1,0,1,0,0,1,1,1,1,1,0,1,1,0,1,1,1,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,0,1,1,0,0,1,0,0,0,0,0,0,1,0,0,1,1,0,1,0,0,0,1,0,0,1,0,1,0,0,1,1,1,0,1,1,1,1,1,1,0,0,0,1,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,1,1,1,0,1,1,1,1,1,1,0,1,0,0,0,1,1,1,1,0,0,1,0,0,1,1,0,1,1,1,0,0,0,1,0,0,1,0,0,1,0,0,1,1,0,0,0,0,0,1,1,1,0,0,1,1,1,1,0,1,0,0,0,1,0,0,1,1,0,1,0,1,1,0,1,0,1,1,0,0,1,0,1,0,1,0,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,0,1,1,0,1,1,0,0,1,0,0,1,0,1,0,0,1,1,0,1,0,0,1,0,1,1,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,0,1,0,0,1,0,0,1,1,1,0,0,0,0,0,0,0,1,0,0,1,0,1,1,1,0,1,0,1,0,0,1,1,1,1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,1,0,0,1,0,0,1,0,1,0,1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,1,0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,1,0,1,0,1,0,0,1,0,0,1,0,0,1,0,0,1,1,1,1,1,0,0,0,1,0,0,0,1,1,1,1,0,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,0,0,1,1,0,1,1,0,0,0,1,0,1,1,0,0,1,1,1,1,1,0,0,0,0,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,0,0,1,0,0,0,1,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,1,0,1,0,0,0,0,0,1,1,0,1,0,1,0,1,1,1,1,1,1,0,1,1,1,0,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0,1,0,1,1,0,1,1,0,1,0,0,0,1,1,0,1,0,1,0,1,0,0,1,0,0,1,1,1,0,0,1,1,0,1,0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0,1,1,0,0,1,0,1,0,1,1,0,1,0,0,0,0,1,1,1,0,1,0,1,1,1,0,0,0,0,0,0,1,0,1,1,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,1,1,1,0,1,0,1,0,0,1,0,0,0,1,1,1,1,0,0,1,1,0,1,0,1,1,0,1,1,0,0,1,1,1,1,0,0,1,0,0,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,0,0,0,1,1,0,1,1,0,0,1,1,1,1,1,0,0,1,0,0,0,1,0,0,1,1,0,1,0,0,1,1,0,1,0,0,0,0,1,1,0,0,1,0,1,0,0,1,1,1,0,0,0,1,1,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,1,1,0,1,1,0,1,0,0,1,1,1,1,1,1,1,0,0,1,1,0,1,0,1,1,0,1,1,1,0,0,1,1,0,1,1,0,0,1,0,1,1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,0,1,1,0,1,1,0,1,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,0,0,1,1,0,0,1,0,1,1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,1,0,0,0,1,1,1,0,0,1,0,0,1,0,1,1,0,1,1,0,1,1,0,1,0,0,1,0,1,0,1,0,1,1,0,0,0,1,1,1,0,1,1,0,1,1,0,0,1,0,0,0,0,1,0,0,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,1,1,1,0,0,1,1,0,1,0,0,1,1,0,1,1,1,0,1,0,1,1,0,1,0,0,0,0,1,1,1,1,0,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,1,1,0,1,0,0,0,1,0,0,0,1,1,1,1,0,1,0,1,1,1,1,0,1,1,0,0,1,0,1,1,1,1,1,0,1,1,0,0,0,0,1,0,0,1,1,0,0,1,1,0,0,0,0,0,1,1,0,1,0,1,0,0,1,1,0,1,1,0,0,1,0,1,0,1,0,0,0,0,1,0,1,1,1,0,0,1,0,0,1,0,1,0,1,1,0,1,1,1,0,1,1,0,0,0,0,1,0,1,0,0,1,1,0,1,0,1,1,1,0,0,0,1,1,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,1,0,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,1,1,0,0,1,1,1,1,0,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,1,0,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,1,1,0,0,1,1,1,1,0,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,1,0,1,0,1,0,0,1,1,0,1,1,0,0,0,1,1,0,0,0,1,0,0,0,1,0,1,1,1,0,0,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,1,0,0,0,1,0,0,1,1,1,1,0,0,0,1,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,0,0,1,0,1,1,0,1,0,1,0,0,1,1,0,0,1,0,1,1,0,1,0,0,0,1,0,1,1,0,1,0,0,1,1,0,0,1,0,0,1,0,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,1,0,1,0,1,0,0,1,1,1,0,1,1,1,0,0,1,1,1,1,0,1,0,0,0,1,1,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,1,0,1,0,0,0,0,0,1,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,1,1,1,1,0,0,0,1,1,1,1,1,0,1,0,0,1,1,1,1,0,0,0,0,0,0,1,0,1,1,1,1,0,0,1,1,0,1,1,0,0,1,0,1,1,0,1,0,0,0,0,0,0,1,0,0,1,1,0,1,1,1,0,0,0,0,0,0,1,0,0,1,1,0,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,1,0,1,1,0,1,1,0,1,0,0,1,0,1,1,1,1,1,1,0,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,1,1,1,0,1,0,0,0,0,0,1,1,0,1,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1,1,0,0,1,1,0,0,1,1,1,1,1,0,1,0,1,0,0,1,1,1,1,0,1,0,0,0,1,1,1,0,0,1,1,0,1,1,0,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1,1,1,0,1,1,0,0,1,0,0,0,1,1,0,1,0,1,1,0,0,0,1,0,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,1,1,1,1,0,0,1,0,0,0,1,1,0,1,0,1,1,0,1,0,0,0,0,0,1,0,0,0,1,1,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,0,1,1,1,0,1,1,1,0,0,1,1,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,1,1,1,0,1,0,1,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,1,0,0,1,0,1,1,0,0,0,1,0,1,1,0,0,1,1,0,0,1,0,0,1,1,1,0,1,0,1,0,0,0,1,1,1,0,1,1,1,1,0,1,0,1,0,1,1,1,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0,1,0,1,0,0,0,0,0,0,1,1,1,1,0,0,0,1,0,1,0,0,1,1,0,1,1,0,1,1,0,0,1,1,1,1,1,0,0,1,0,1,0,0,1,0,0,0,1,1,1,1,0,1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,1,1,0,1,0,1,0,0,0,0,0,1,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,0,0,1,0,0,0,1,1,0,1,1,0,1,1,0,0,1,1,1,1,0,0,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,1,0,1,0,0,0,0,0,1,0,0,1,1,0,1,1,1,1,1,0,0,0,0,1,0,1,0,1,1,0,1,0,1,1,1,1,0,0,1,1,0,0,1,1,0,1,1,0,1,0,0,1,1,1,0,0,1,0,1,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,1,1,1,0,1,1,1,1,0,0,1,0,1,1,1,1,0,1,0,0,0,0,1,1,1,1,1,0,1,0,1,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,1,1,0,1,0,1,1,1,1,0,1,0,0,0,1,1,0,1,0,1,1,1,0,1,0,0,0,0,0,0,1,1,1,0,0,0,1,0,0,0,1,1,0,0,0,0,1,0,0,0,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,1,0,1,0,1,0,0,1,1,0,0,0,0,0,1,1,0,1,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,0,1,0,0,1,0,1,1,1,1,0,0,1,0,1,1,1,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,1,1,1,1,0,0,1,0,0,0,1,1,0,1,0,0,0,0,1,1,0,0,0,0,0,1,0,1,1,0,0,1,0,1,0,0,1,1,1,0,1,1,0,0,1,0,0,0,1,1,0,0,1,0,0,0,1,1,0,0,1,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,1,0,0,1,1,0,0,0,1,0,0,1,1,1,1,0,0,0,1,1,1,0,0,0,1,1,0,0,1,1,0,1,1,1,1,1,0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,1,1,0,0,1,1,1,0,0,1,1,0,0,1,1,0,1,0,0,1,0,1,1,1,1,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,0,0,1,1,0,0,1,0,0,0,0,0,1,1,0,1,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,0,1,1,1,1,0,1,1,0,0,1,1,0,0,1,0,0,1,1,1,0,1,0,1,0,1,0,1,1,0,1,1,0,0,0,0,1,0,0,0,1,1,1,1,1,0,0,1,1,1,0,1,0,0,0,1,1,0,0,0,1,0,0,1,0,1,1,1,1,0,1,0,1,1,0,1,0,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,1,0,1,1,1,1,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,0,0,0,1,0,1,1,1,0,0,1,1,0,0,0,0,1,1,0,1,1,0,0,1,0,0,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,1,1,1,0,1,1,0,0,1,0,0,1,0,0,1,0,1,0,1,1,1,1,0,0,1,0,1,1,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,0,0,1,0,0,0,1,0,0,0,1,0,1,1,0,1,1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,1,1,0,0,0,1,1,0,0,0,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,0,1,1,0,0,0,0,1,1,0,1,1,1,0,1,0,1,1,0,0,0,1,1,0,1,1,1,1,1,0,1,0,0,0,0,0,1,1,0,1,1,1,1,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,1,1,0,1,0,1,0,1,0,0,1,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1,0,1,1,1,1,0,1,0,0,1,0,1,0,1,1,0,0,1,0,1,0,1,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,1,0,0,0,0,1,0,1,0,1,0,1,0,0,1,1,0,0,0,0,1,0,1,1,1,0,0,1,1,0,1,0,1,0,0,0,1,1,1,1,1,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0,0,1,0,1,1,0,1,1,1,1,0,0,1,0,0,0,1,1,0,0,1,1,0,1,1,0,1,1,1,1,0,1,1,0,0,1,1,0,0,0,0,1,1,0,1,1,1,1,0,0,0,0,1,1,0,1,1,0,1,1,1,1,1,0,0,1,0,0,1,0,1,1,0,0,0,1,0,1,1,1,1,0,1,1,0,0,1,1,0,1,0,1,0,1,0,0,0,1,1,1,1,0,1,1,0,1,0,0,0,0,0,1,1,0,0,1,0,0,0,1,0,1,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,1,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,1,0,0,0,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,0,1,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,1,0,1,0,1,0,0,1,1,0,1,1,0,1,0,0,0,0,0,1,0,1,1,1,1,0,0,1,0,0,1,0,0,1,0,1,0,0,0,1,1,0,1,0,0,1,1,1,1,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1,1,0,1,0,0,0,1,1,1,1,1,0,0,1,0,1,1,1,1,0,0,1,1,0,1,0,1,1,0,0,0,1,0,1,0,0,1,1,0,0,1,0,0,1,1,1,1,1,1,1,0,1,0,0,1,0,0,1,1,1,1,1,1,0,1,0,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0,0,0,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,1,0,1,1,1,0,1,1,0,0,0,0,0,1,0,1,0,1,1,1,1,1,0,1,1,0,1,1,0,0,1,1,0,0,1,0,1,0,0,1,0,0,0,0,0,1,0,1,1,1,1,1,0,1,1,0,1,0,0,1,1,0,0,1,1,0,0,0,0,0,1,0,0,0,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,0,0,0,1,0,1,1,1,0,0,0,0,0,1,1,0,1,0,0,1,0,0,0,0,1,1,1,1,0,1,1,0,0,1,0,1,1,0,1,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,1,0,1,1,1,0,0,0,1,1,1,1,0,1,0,1,1,0,1,0,0,1,1,0,0,1,1,0,0,1,0,0,0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,0,1,0,0,1,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,1,0,0,1,1,0,0,0,0,0,1,0,1,1,0,0,1,1,1,0,0,1,0,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,0,0,1,1,0,1,1,0,0,0,0,1,1,1,1,1,0,1,0,1,1,0,1,1,1,0,1,1,0,1,0,1,0,0,0,0,1,0,1,0,0,1,1,0,0,1,1,1,0,0,0,1,1,1,1,0,1,0,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,1,0,1,0,1,1,1,1,0,0,0,1,1,0,1,1,1,0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0,0,0,0,1,1,0,0,1,1,1,0,1,1,0,1,0,0,0,1,1,0,0,0,1,1,1,1,0,0,1,1,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,1,1,0,1,1,0,1,0,0,1,0,0,0,0,0,0,1,1,1,0,0,0,1,0,0,1,1,1,1,1,1,1,0,1,1,0,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1,1,0,1,1,0,1,0,0,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,1,1,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,0,1,0,1,0,1,0,0,1,1,0,1,0,1,1,1,1,0,0,1,0,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,1,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,1,0,0,0,1,1,1,1,0,0,1,1,1,0,0,0,1,1,1,1,0,0,1,0,0,0,1,1,0,0,0,1,1,1,1,1,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,1,0,1,1,1,1,0,1,1,0,0,0,0,1,1,0,1,0,0,1,0,0,1,0,1,1,0,1,0,0,0,1,1,0,1,1,1,1,0,1,0,0,1,0,0,1,0,1,1,0,1,1,0,1,0,1,0,1,1,0,0,0,1,1,1,0,1,0,1,1,1,1,0,1,0,0,0,0,1,1,0,1,1,1,0,0,1,1,0,0,1,0,0,0,1,1,1,1,1,0,1,0,1,0,0,1,1,0,0,0,1,0,0,0,1,0,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,0,1,1,0,0,1,1,1,0,0,1,0,0,1,1,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,1,0,1,1,0,1,1,0,1,1,0,0,1,0,0,1,0,1,1,1,1,0,1,1,0,0,0,0,1,0,1,0,1,0,0,0,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,1,1,1,0,0,1,0,0,0,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,0,0,1,0,1,0,1,1,1,0,1,0,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,0,1,1,1,1,0,0,0,0,0,1,1,0,1,0,1,1,1,1,0,1,0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,1,1,1,0,0,1,0,0,1,0,0,0,0,1,1,1,0,1,1,0,0,0,0,0,0,0,1,1,0,1,1,1,1,0,1,0,1,0,0,0,1,1,1,0,1,0,1,1,0,0,0,0,0,0,1,0,0,1,1,0,1,0,1,1,0,0,0,0,0,0,1,0,0,0,0,1,0,1,1,0,0,1,0,1,1,0,1,0,0,1,0,1,0,0,0,0,0,1,1,0,0,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,0,1,1,0,1,1,0,1,0,0,0,0,0,1,1,1,1,1,1,0,1,0,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,1,1,1,1,1,1,1,0,1,0,1,1,0,1,0,0,1,1,1,0,0,0,1,0,0,1,1,0,0,0,0,0,0,1,1,1,0,1,1,0,1,0,1,1,0,0,1,1,0,1,1,0,0,1,1,0,1,1,0,1,0,0,0,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1,0,1,0,1,0,0,0,1,1,1,0,0,1,1,0,0,0,0,0,1,1,0,1,1,0,0,0,1,1,0,1,1,1,0,1,1,0,1,1,1,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,1,0,0,1,1,0,1,1,0,0,1,1,0,1,1,0,1,0,1,0,0,1,0,1,1,0,1,1,0,1,1,0,0,1,1,1,1,0,0,1,1,0,0,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,0,1,1,0,1,0,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,1,0,0,0,0,0,1,1,0,0,0,1,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,0,0,1,1,0,1,1,1,0,1,1,0,1,0,1,1,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0,1,1,0,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,0,1,1,0,0,1,1,1,0,1,0,1,1,1,0,0,0,1,1,1,0,1,1,0,1,0,0,0,1,0,0,0,0,1,1,1,1,0,0,0,0,0,1,0,1,1,0,1,1,1,1,0,0,0,0,0,1,1,1,1,0,1,0,0,1,1,1,0,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,0,0,0,1,0,1,1,0,1,1,1,0,1,0,0,1,0,1,1,1,1,0,1,0,0,1,1,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,1,0,0,0,1,1,1,1,1,0,1,1,1,0,0,1,1,1,1,0,1,1,0,1,0,0,0,0,1,1,1,0,1,0,1,0,1,0,1,1,0,1,1,0,0,0,0,1,0,0,1,0,0,0,0,1,1,1,0,1,1,1,0,0,0,1,1,0,0,1,0,1,0,0,0,0,1,1,0,0,1,1,0,1,1,1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1,0,1,0,0,0,0,1,1,1,0,0,1,0,1,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,1,0,1,0,1,1,0,1,1,1,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,1,1,0,0,1,1,0,0,0,0,1,0,0,0,1,0,1,0,0,1,1,0,1,0,1,0,1,1,1,1,0,1,1,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,0,0,0,1,1,1,1,0,1,1,0,0,1,0,0,0,0,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,0,1,0,0,0,1,0,1,1,1,1,1,1,0,0,0,1,0,0,1,0,1,1,1,1,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,0,1,0,1,0,1,1,1,1,1,0,0,1,1,0,1,1,1,0,1,1,0,0,1,1,1,1,0,1,0,0,0,0,0,1,0,1,1,0,0,1,0,1,1,1,1,0,1,0,0,1,1,1,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,0,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,0,0,1,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,0,1,1,0,1,1,1,0,1,0,1,0,1,1,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,0,1,0,1,1,1,0,1,0,0,0,1,1,0,1,1,1,1,0,1,1,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,1,0,1,0,1,1,0,1,1,1,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,1,1,1,1,1,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,0,0,1,0,1,0,0,0,1,0,0,1,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,0,1,0,1,1,0,0,1,0,1,0,0,1,0,0,0,0,1,1,0,1,1,0,1,0,0,1,1,1,0,1,1,1,0,0,1,1,1,1,1,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,0,0,1,1,1,0,1,0,0,0,1,1,1,0,0,0,0,1,1,0,0,1,0,0,1,0,1,0,1,1,0,1,1,0,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,0,0,1,0,0,1,0,1,1,0,1,0,1,1,0,1,1,0,1,1,0,0,1,1,1,0,1,1,1,0,0,0,1,0,0,0,0,0,0,1,1,0,1,1,1,0,1,0,0,0,0,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1,0,0,1,1,0,0,1,0,1,1,1,0,0,1,0,1,1,0,1,0,1,0,0,0,1,1,0,1,0,0,0,0,0,1,0,1,1,0,1,1,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,0,1,1,0,1,0,1,1,1,0,1,1,0,0,1,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,1,1,0,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,1,1,0,0,1,1,1,1,0,0,0,1,0,0,1,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0,0,0,1,0,0,0,0,0,1,1,0,1,1,0,1,1,1,0,0,1,1,0,1,1,0,0,0,0,0,1,0,1,1,0,1,0,0,0,1,1,1,0,1,1,1,0,1,0,1,0,0,1,1,1,1,1,0,1,1,0,1,1,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,1,1,1,0,1,0,0,1,1,0,1,1,1,0,0,1,0,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,1,0,1,1,1,0,0,1,1,0,1,0,1,1,0,0,1,1,0,0,0,0,0,0,1,0,1,0,0,1,1,1,1,0,0,1,1,0,1,0,0,1,0,0,0,0,1,1,0,0,0,1,0,1,0,0,0,1,1,1,1,1,0,0,1,1,0,1,0,1,1,0,1,1,1,0,0,1,1,0,0,0,1,1,1,1,0,1,0,1,0,0,1,0,1,1,1,1,1,0,1,0,1,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,1,1,1,1,0,0,0,1,0,1,1,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,1,0,1,1,1,1,1,0,0,0,1,0,1,0,1,1,1,0,0,1,0,1,0,1,1,1,0,0,0,1,0,1,0,0,1,1,0,0,0,0,1,1,0,1,1,0,0,1,1,0,1,0,1,0,0,1,1,0,0,0,0,1,0,1,0,0,1,1,1,1,1,0,1,0,1,1,0,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,1,1,1,1,1,0,1,1,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1,1,0,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,1,0,1,1,0,1,0,0,0,1,1,1,1,0,0,0,1,1,0,1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,1,1,1,0,1,1,1,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,1,1,1,0,1,1,1,0,1,0,0,1,0,0,1,1,1,1,0,0,0,1,1,0,0,0,1,0,1,0,0,0,1,1,1,1,0,0,1,1,1,1,0,1,0,0,0,0,1,1,1,0,1,0,1,1,0,0,1,1,0,0,1,0,0,0,1,0,1,0,1,0,0,1,1,0,0,0,0,0,1,0,0,1,0,1,1,1,0,0,1,0,1,0,0,0,0,0,0,1,0,0,1,0,1,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,1,0,1,0,0,0,1,1,1,0,1,0,0,0,1,0,0,0,1,1,1,0,0,1,1,0,0,1,0,0,1,0,1,1,0,0,0,0,0,1,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,1,0,0,0,0,1,0,1,0,1,1,0,1,1,0,1,0,0,1,0,0,1,1,1,0,1,1,1,0,1,1,1,0,0,1,0,1,1,0,1,0,0,0,1,0,0,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,1,0,1,1,0,0,1,0,0,0,0,1,1,0,1,1,1,1,0,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,1,0,0,1,0,0,1,1,0,0,0,1,1,0,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,0,0,1,0,0,0,1,0,1,1,1,1,1,1,0,1,1,0,0,1,1,1,0,1,0,0,1,0,0,1,1,0,0,0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,0,0,1,1,0,0,0,0,0,1,0,1,1,1,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,1,0,1,1,0,0,0,0,1,1,1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,1,1,0,0,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0,0,0,1,0,0,1,0,0,0,0,1,1,1,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0,1,1,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1,0,0,1,0,1,1,0,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,1,0,1,0,0,1,1,1,1,0,1,0,1,1,1,0,1,1,0,1,0,1,1,0,1,1,0,1,1,1,0,0,0,1,0,0,0,1,1,1,1,0,0,1,0,0,0,0,0,1,1,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,0,0,0,1,1,0,0,0,1,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1,1,0,0,0,1,0,0,1,0,1,1,1,1,0,0,0,1,0,1,1,0,0,1,0,1,0,0,0,0,0,0,0,1,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,1,1,0,0,1,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,1,0,1,0,1,1,0,1,0,0,0,1,1,1,0,0,0,1,0,0,1,0,1,0,1,1,1,1,0,1,0,1,0,0,0,1,1,1,0,0,1,0,1,1,1,1,0,0,1,1,0,1,1,0,0,1,0,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,1,0,0,1,1,0,1,0,1,1,1,0,0,1,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,0,0,1,1,0,0,1,0,1,0,0,1,1,1,0,1,0,0,0,1,1,1,1,0,1,1,1,0,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,0,1,0,0,0,0,1,1,0,0,0,1,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,1,0,0,1,1,1,1,0,1,1,1,1,1,1,0,0,1,0,1,0,1,1,0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,0,1,1,0,1,1,1,0,0,0,0,0,1,1,0,1,1,1,1,1,0,0,1,1,0,1,1,1,0,0,1,1,1,0,1,1,0,1,0,1,1,0,0,1,0,0,1,1,1,0,0,0,1,1,0,1,1,0,0,1,1,0,1,0,0,0,1,0,0,1,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,1,1,1,1,1,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,1,1,0,0,1,1,0,1,1,0,0,1,1,1,0,0,1,1,1,0,1,1,0,0,0,1,0,0,1,0,1,0,0,1,1,1,0,0,1,1,0,1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,1,0,1,1,1,1,0,0,0,1,0,1,1,0,1,1,0,1,1,0,1,0,1,0,0,1,0,0,1,0,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,0,0,1,0,1,1,0,0,1,1,1,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,1,0,1,1,1,0,1,1,0,1,0,1,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,1,0,0,0,0,1,1,0,1,0,1,1,1,1,1,1,0,0,0,1,1,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,1,0,1,1,0,1,0,0,1,1,1,1,0,1,1,1,0,1,0,1,0,0,1,0,0,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,1,0,1,1,0,1,1,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,1,0,0,1,0,1,1,0,0,1,1,1,1,1,1,0,1,0,1,0,0,1,1,1,0,1,0,0,1,0,0,1,0,0,1,0,1,1,1,0,1,1,0,0,1,0,1,1,1,0,0,0,1,0,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,1,1,0,1,0,0,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,1,1,1,1,1,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,1,1,1,0,1,0,0,0,0,1,0,0,0,1,0,0,1,1,0,1,0,1,1,0,0,0,1,0,1,1,1,0,0,1,0,1,1,1,0,0,1,1,1,0,1,0,1,0,0,0,1,0,1,1,1,0,0,1,1,1,0,1,0,0,0,1,1,1,0,1,0,0,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1,1,1,1,1,1,1,0,1,1,0,1,0,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,1,0,0,0,1,0,1,1,0,1,1,1,1,0,0,0,1,1,1,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,0,0,1,1,0,1,0,0,1,1,1,0,1,1,0,0,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,1,1,1,0,0,1,1,0,1,1,0,1,1,1,0,1,0,0,0,1,1,0,1,0,1,0,1,1,0,1,1,0,0,1,1,0,1,1,1,1,1,0,0,1,1,1,0,0,0,0,1,1,0,0,1,0,0,1,0,0,0,0,1,1,1,1,1,1,0,0,1,1,0,0,0,0,1,0,1,1,1,0,1,1,0,1,0,0,0,0,0,1,0,1,1,0,0,1,1,0,1,1,0,0,1,1,1,0,1,1,1,1,1,1,0,0,1,1,1,1,0,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,0,0,0,1,1,1,0,1,0,0,0,1,0,1,1,1,0,1,0,0,0,0,1,1,0,0,1,1,0,1,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,1,1,0,0,1,0,0,1,1,0,1,1,0,0,0,1,0,1,1,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,1,1,0,1,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,1,0,1,1,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1,1,0,0,0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,0,1,1,1,1,1,0,0,1,1,1,0,1,1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,1,1,0,1,0,0,0,1,1,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,1,0,1,0,1,1,0,0,0,0,0,1,0,0,0,0,1,1,0,0,1,0,0,1,0,1,0,0,0,1,0],3375))
print('should be 6799')