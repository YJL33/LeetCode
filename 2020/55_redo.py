"""
55
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, ans = 0, 0
        while i <= ans and i < len(nums):
            ans = max(ans, i+nums[i])
            i += 1
        return i == len(nums)