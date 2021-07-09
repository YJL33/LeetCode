"""
915
"""
from typing import List
import collections
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        # update 2 arr
        lmax, rmin = 0, []
        for n in nums[::-1]:
            rmin.append(min(rmin[-1] if rmin else float('inf'), n))
        rmin.reverse()

        for i in range(len(nums)-1):
            lmax = max(lmax, nums[i])
            if lmax <= rmin[i+1]:
                return i+1
        
        return