from typing import List
class Solution:
    def removeDuplicates(self, A: List[int]) -> int:
        # 1. check the duplication
        # 2. craft the array
        # by observation: we can combine above into one
        if not A: return
        
        k, prev = 1, A[0]
        for a in A[1:]:
            if a != prev:
                A[k] = a
                prev = a
                k += 1
        return k
