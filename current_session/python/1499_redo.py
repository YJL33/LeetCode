# Return the maximum value of the equation yi + yj + |xi - xj| 
# where |xi - xj| <= k and 1 <= i < j <= points.length.

# use sliding window + heap
# for all xi, xj => xj > xi
# we're looking for 
#       max value of yi + yj + xj - xi = (xj+yj)+ (yi-xi)
#    => max (yi-xi) => min (xi-yi) for each j
# where xj - xi <= k


from typing import List
import heapq
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        h = []                  # push (xi-yi, xi)
        res = float('-inf')
        for x, y in points:
            while h and x-h[0][-1] > k:
                # maintain the size of heap
                heapq.heappop(h)
            if h:
                tmp = h[0][0]               # min xi-yi
                res = max(res, x+y-tmp)     # xj+yj-(xi-yi) = xj+yj+yi-xi
            heapq.heappush(h, (x-y, x))
        return res