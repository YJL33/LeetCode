# use dp
from typing import List
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        rgb = costs[0]
        for i in range(1,len(costs)):
            r = min(rgb[1],rgb[2])+costs[i][0]
            g = min(rgb[0],rgb[2])+costs[i][1]
            b = min(rgb[0],rgb[1])+costs[i][2]
            rgb = [r,g,b]
        return min(rgb)

