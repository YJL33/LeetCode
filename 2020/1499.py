"""
1499
"""
from typing import List
import heapq
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # find max yi+yj+|xi-xj|
        # sliding window width=k
        # xi<xj for all i<j => yi+yj+|xi-xj| = yi+yj+xj-xi = (xj+yj)+(-xi+yi)
        # => find max(-xi+yi) for each j

        h = []                  # min-heap, store (x-y, x)
        ans = float('-inf')
        for x, y in points:
            while h and x-h[0][1] > k:
                heapq.heappop(h)
            if h:
                ans = max(ans, x+y-h[0][0])
            heapq.heappush(h, (x-y, x))
        return ans


print(Solution().findMaxValueOfEquation(points = [[1,3],[2,0],[5,10],[6,-10]], k = 1))
print(Solution().findMaxValueOfEquation(points = [[0,0],[3,0],[9,2]], k = 3))
print('should be 4,3,399134490')