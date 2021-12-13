from typing import List
class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        l, r = 0, len(plants)-1
        remainingA, remainingB = capacityA, capacityB
        cnt = 0
        while l < r:
            if plants[l] <= remainingA:
                remainingA -= plants[l]
            else:
                remainingA = capacityA-plants[l]
                cnt += 1
            if plants[r] <= remainingB:
                remainingB -= plants[r]
            else:
                remainingB = capacityB-plants[r]
                cnt += 1
            l, r = l+1, r-1
        
        if l == r:
            cnt += 1 if max(remainingA, remainingB) < plants[l] else 0
        
        return cnt

