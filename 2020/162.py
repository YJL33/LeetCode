"""
162
"""
class Solution:
    def findPeakElement(self, A: List[int]) -> int:
        prev = 0
        for i in range(1,len(A)):
            if A[prev] > A[i]:
                return prev
            else:
                prev = i
        return prev