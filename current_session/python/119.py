
# e.g. rowIndex = 3 => 1 3 3 1 => 4 numbers
# e.g. rowIndex = 4 => 1 4 6 4 1 => 5 numbers
# dp: f(n) = f(n-1) + ([0]+f(n-1))
# 

from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [0 for _ in range(rowIndex+1)]    # r+1 numbers, e.g. r=3, range(4) = [0,1,2,3]
        res[0] = 1
        
        for i in range(1,rowIndex+1):
            # each round, start at 1, end at i (last index added)
            # reverse to avoid polluting res
            for j in range(i, 0, -1): res[j] += res[j-1]
        return res

print(Solution().getRow(0))
print(Solution().getRow(3))
print(Solution().getRow(4))
print(Solution().getRow(5))