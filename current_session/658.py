"""
658
"""
from typing import List
class Solution:
    def findClosestElements(self, A: List[int], k: int, x: int) -> List[int]:
        # use heap, import min heap library => O(nlogn)
        # use binary search
        # we want to find m such that minimize the sum of (A[m]-x) & (A[m+k]-x)
        l, r = 0, len(A)-k
        while l < r:
            m = (l+r)/2
            if x-A[m] > A[m+k]-x:
                l = m+1
            else:
                r = m
        return A[l:l+k]