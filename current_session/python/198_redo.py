from typing import List
class Solution:
    def rob(self, A: List[int]) -> int:
        dpRob = A[0]
        dpNoRob = 0
        for i in range(1,len(A)):
            dpRob, dpNoRob = dpNoRob+A[i], max(dpRob, dpNoRob)
        return max(dpNoRob, dpRob)
        