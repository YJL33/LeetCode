"""
1610
"""
from typing import List
import math
import bisect
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        # calculate the angle of each point
        # then use sliding window to find max num of visible points
        x, y = location
        angles = []         # angle of each point to location, x axis = 0
        copoint = 0         # number of copoint with location
        for p in points:
            x2, y2 = p
            if x==x2 and y==y2:
                copoint += 1
                continue
            angles += (180+math.atan2(y2-y, x2-x)*180/math.pi),
        angles.sort()
        angles = angles + [a+360 for a in angles]       # to cover cases like: deg=5, pts=[1, 359]
        # print('angles:',angles)
        
        start, ans = 0, 0
        for i in range(len(angles)):
            if angles[i] == start: continue
            start, end = angles[i], angles[i]+angle
            r = bisect.bisect_right(angles, end)
            # print('now:', start, end, i, r)
            ans = max(ans, r-i)
        
        return min(ans, len(points))+copoint
            
print(Solution().visiblePoints([[2,1],[2,2],[3,3]],90,[1,1]), 'should be 3')
print(Solution().visiblePoints([[2,1],[2,2],[3,4],[1,1]],90,[1,1]), 'should be 4')
print(Solution().visiblePoints([[1,0],[2,1]],13,[1,1]), 'should be 1')
print(Solution().visiblePoints([[1,1],[2,2],[1,2],[2,1]],0,[1,1]), 'should be 2')
print(Solution().visiblePoints([[0,0],[0,2]],90,[1,1]), 'should be 2')
print(Solution().visiblePoints([[1,1],[2,2],[3,3],[4,4],[1,2],[2,1]],0,[1,1]), 'should be 4')
print(Solution().visiblePoints([[1,1],[1,1],[1,1]],1,[1,1]), 'should be 3')
