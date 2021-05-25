'''
1465

Given a rectangular cake with height h and width w,
and two arrays of integers horizontalCuts and verticalCuts
where horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut
and similarly, verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

Return the maximum area of a piece of cake
after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts.
Since the answer can be a huge number, return this modulo 10^9 + 7.

Constraints:

2 <= h, w <= 10^9
1 <= horizontalCuts.length < min(h, 10^5)
1 <= verticalCuts.length < min(w, 10^5)
1 <= horizontalCuts[i] < h
1 <= verticalCuts[i] < w
It is guaranteed that all elements in horizontalCuts are distinct.
It is guaranteed that all elements in verticalCuts are distinct.

'''
from typing import List
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # simply find the max diff in hCut and vCut then multiply them together
        horizontalCuts.sort()
        verticalCuts.sort()
        mgH, mgV = horizontalCuts[0], verticalCuts[0]
        horizontalCuts.append(h)
        verticalCuts.append(w)
        for i in range(1,len(horizontalCuts)):
            mgH = max(mgH, horizontalCuts[i]-horizontalCuts[i-1])
        for j in range(1,len(verticalCuts)):
            mgV = max(mgV, verticalCuts[j]-verticalCuts[j-1])
        # print(mgH, mgV)
        return (mgH*mgV)%(1000000007)

print(Solution().maxArea(h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]))
print(Solution().maxArea(h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]))
print(Solution().maxArea(h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]))