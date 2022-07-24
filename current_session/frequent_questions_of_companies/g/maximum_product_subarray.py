# use greedy
# update localMin, localMax, globalMax
from typing import List
class Solution:
    def maxProduct(self, A:List[int]) -> int:
        localMin, localMax, globalMax = A[0], A[0], A[0]
        for a in A[1:]:
            localMin, localMax = min(a*localMax, a*localMin, a), max(a*localMax, a*localMin, a)
            globalMax = max(localMax, globalMax)
        return globalMax

print(Solution().maxProduct([2,3,-2,4]))
print(Solution().maxProduct([-2,0,-1]))