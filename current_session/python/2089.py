from typing import List
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        tgtCnt = 0
        prevCnt = 0
        for n in nums:
            if n == target:
                tgtCnt += 1
            elif n < target:
                prevCnt += 1
        
        if tgtCnt == 0:
            return []
        else:
            return [x for x in range(prevCnt, prevCnt+tgtCnt)]
                