"""
https://leetcode.com/problems/minimum-size-subarray-sum/
"""
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # naive approach: pick all i, j,  O(n^3)
        # sliding window
        if not nums: return 0
        width = len(nums)+1
        l, r = 0, 1
        while r <= len(nums) and l < len(nums):
            if r-l > width:
                l += 1
            # optimization: keep update a sum instead of sum everytime
            elif sum(nums[l:r]) >= s:
                width = r-l
                l += 1
            elif sum(nums[l:r]) < s:
                r += 1
            # print('l, r', l, r, nums[l:r])
        if width == len(nums)+1: return 0
        return width
        
print(Solution().minSubArrayLen(s = 7, nums = [2,3,1,2,4,3]))