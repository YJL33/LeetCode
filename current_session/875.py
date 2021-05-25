"""
875
"""
from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # use bisect?
        piles.sort()
        l, r = 1, piles[-1]

        def getH(k):
            hh = 0
            for p in piles:
                hh += math.ceil(p/k)
            return hh

        while l < r:
            m = (l+r)//2
            if getH(m) <= h:         # m is too big
                r = m
            else:
                l = m+1
        return l

print(Solution().minEatingSpeed(piles = [3,6,7,11], h = 8))
print(Solution().minEatingSpeed(piles = [30,11,23,4,20], h = 5))
print(Solution().minEatingSpeed(piles = [30,11,23,4,20], h = 6))