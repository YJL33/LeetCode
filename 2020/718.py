"""
718
"""
from typing import List
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        # dp[i][j] = length of longest common array of A[:i+1] and B[:j+1]
        dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
        res = 0
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    res = max(res, dp[i][j])
        # print(dp)
        return res