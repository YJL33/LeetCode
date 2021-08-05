from typing import List
class Solution:
    def removeDuplicates(self, A: List[int]) -> int:
        # 1st pass: count k
        # 2nd pass: craft the array
        # by observation: we can combine above into one
        if not A: return
        
        k, tail = 1, A[0]
        for a in A[1:]:
            if a != tail:
                A[k] = a
                tail = a
                k += 1
        return k

