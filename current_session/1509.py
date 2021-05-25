"""
1509
"""
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4: return 0
        nums.sort()
        l, r = 0, len(nums)-3
        res = float('inf')
        while r <= len(nums):
            res = min(res, nums[r-1]-nums[l])
            l, r = l+1, r+1
        
        return res