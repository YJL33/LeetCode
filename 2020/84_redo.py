"""
84
"""
from typing import List
class Solution:
    def largestRectangleArea(self, A: List[int]) -> int:
        st = [len(A)]
        A += 0,
        ans = 0
        for i in range(len(A)):
            while A[i] < A[st[-1]]:
                H = A[st.pop()]
                W = i-st[-1]-1
                ans = max(ans, H*W)
            stack += i,
        return ans