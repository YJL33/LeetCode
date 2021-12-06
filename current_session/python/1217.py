from typing import List
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # eventually all positions can cascade into 2 consecutive positions
        oddCnt, evenCnt = 0, 0
        for p in position:
            if p%2:
                oddCnt += 1
            else:
                evenCnt += 1
        
        return min(oddCnt, evenCnt)
