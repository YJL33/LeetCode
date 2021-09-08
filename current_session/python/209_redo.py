# min size subarray sum

# use sliding window
# keep increase r
# find subarray sum >= target including A[r] by keep shrinking l

from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target > sum(nums) or target < min(nums): return 0
        l, subSum, ans = 0, 0, float('inf')
        for r in range(len(nums)):
            subSum += nums[r]
            while l < r and subSum-nums[l] >= target:       # minimize the sub array
                subSum -= nums[l]
                l += 1
            if subSum >= target:
                # print('gocha:', r, l)
                ans = min(ans, r-l+1)
        
        return ans

print(Solution().minSubArrayLen(7, [2,1,3,1,2,4,3]))
print(Solution().minSubArrayLen(4, [1,4,4]))
print(Solution().minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
print(Solution().minSubArrayLen(11,[1,2,3,4,5]))
