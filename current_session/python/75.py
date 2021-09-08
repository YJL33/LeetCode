
from typing import List
class Solution:
    def sortColors(self, A: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = -1, len(A)
        for i in range(len(A)):
            if A[i] == 0:
                l += 1
            elif A[i] == 2:
                r -= 1
        
        j = l+1
        while j != r:
            A[j] = 1
            j += 1

        while l >= 0:
            A[l] = 0
            l -= 1
        
        while r < len(A):
            A[r] = 2
            r += 1
        
        return