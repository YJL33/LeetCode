"""
1465
"""
from typing import List
class Solution:
    def maxArea(self, h: int, w: int, hCuts: List[int], vCuts: List[int]) -> int:
        maxH, maxW = 0, 0       # max height and width
        prevH, prevV = 0, 0     # previous horizontal cut and vertical cut
        hCuts.sort()
        vCuts.sort()
        hCuts.append(h)
        vCuts.append(w)
        for hc in hCuts:
            maxH, prevH = max(maxH, hc-prevH), hc

        for vc in vCuts:
            maxW, prevV = max(maxW, vc-prevV), vc
        
        return (maxH*maxW)%(1000000007)

print(Solution().maxArea(h = 5, w = 4, hCuts = [1,2,4], vCuts = [1,3]))
print(Solution().maxArea(h = 5, w = 4, hCuts = [3,1], vCuts = [1]))
print(Solution().maxArea(h = 5, w = 4, hCuts = [3], vCuts = [3]))