"""
45
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf') for _ in nums]
        dp[0] = 0
        for i in range(len(nums)):
            reach = i+nums[i]
            j = i+1
            while j <= reach and j<len(nums):
                dp[j] = min(dp[j], dp[i]+1)
                j += 1
        return dp[-1]