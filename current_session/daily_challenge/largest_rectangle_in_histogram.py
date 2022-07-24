from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # use monotonic (increasing) stack
        # if increasing, add into stack
        # else: pop and check the size until there's no more higher element, then add into stack
        heights.append(0)
        ans, ms = 0, [-1]               # index
        for i, h in enumerate(heights):
            if h < heights[ms[-1]]:
                r = i
                while ms and h < heights[ms[-1]]:
                    ha = heights[ms.pop()]
                    l = ms[-1]
                    ans = max(ans, (r-l-1)*ha)
            ms.append(i)
            # print('ans, i', ans, i, ms)
        return ans

print(Solution().largestRectangleArea([1,2,5,6,2,3]), "== 10")
print(Solution().largestRectangleArea([2,4]), "== 4")
print(Solution().largestRectangleArea([1,2,3,4,5,6,7]), "== 16")
print(Solution().largestRectangleArea([9,5,4,3,2,1]), "== 12")
