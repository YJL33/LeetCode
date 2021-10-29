# simply build a monotonic stack
from typing import List
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ms = []
        for i in range(len(heights)):
            h = heights[i]
            while ms and heights[ms[-1]] <= h:
                ms.pop()
            ms.append(i)
        
        return ms

print(Solution().findBuildings([4,2,3,1]))
print(Solution().findBuildings([4,3,2,1]))
print(Solution().findBuildings([1,3,2,4]))
print(Solution().findBuildings([2,2,2,2]))