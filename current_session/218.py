"""
218
"""
from heapq import heappush, heappop
from typing import List
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # scan from left to right
        # for each 'critical point', maintain a heap to get the skyline
        # note that buildings is sorted by left-i in non-decreasing order

        # l, r = buildings[0][0], 0
        events = []
        for b in buildings:
            # r = max(b[1], r)
            events += (b[0], b[-1]<<1|1),           # new building
            events += (b[1], b[-1]<<1|0),
        events.sort()
        # print(events)
        hp, toRmv = [], []
        skyline = []
        for x, H in events:
            # maintain the heap
            if H%2:
                H = H>>1
                heappush(hp, -1*H)
            else:
                H = H>>1
                heappush(toRmv, -1*H)
            while toRmv and toRmv[0] == hp[0]:
                heappop(hp)
                heappop(toRmv)

            # maintain the skyline
            # print('x, H, hp, tmv', x, H, hp, toRmv)
            while skyline and skyline[-1][0] == x:
                skyline.pop()
            if not hp or not skyline or -1*hp[0] != skyline[-1][-1]:
                skyline += [x, -1*hp[0] if hp else 0],

        return skyline

print(Solution().getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
print(Solution().getSkyline([[0,2,3],[2,5,3]]))
print(Solution().getSkyline([[1,5,3], [1,5,3], [1,5,3]]))
print(Solution().getSkyline([[1,2,1],[1,2,2],[1,2,3]]))