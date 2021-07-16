"""
1793
"""
from typing import List
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # Naive approach, try all L and R, and use a heap to store min(subArray)
        # time complexity O(n^2 logn)
        # think about O(n) approach
        # since the 'good array' must include nums[k]
        # we begin from nums[k]
        ans, minScore, l, r = nums[k], nums[k], k, k
        while l > 0 or r < len(nums)-1:
            if (l == 0):
                r += 1
            elif (r == len(nums)-1):
                l -= 1
            elif (nums[l-1] < nums[r+1]):
                r += 1
            else:
                l -= 1
            minScore = min([minScore, nums[l], nums[r]])
            ans = max(ans, minScore*(r-l+1))
        return ans