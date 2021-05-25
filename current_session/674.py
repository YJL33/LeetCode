"""
674
"""
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums: return 0
        L, cnt, prev = 1, 1, nums[0]
        for n in nums[1:]:
            if n > prev:
                cnt += 1
            else:
                cnt = 1
            prev = n
            L = max(L, cnt)
        return L