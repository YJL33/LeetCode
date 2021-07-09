"""
221
"""
from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp?
        dp = [[int(matrix[i][j]) for j in range(len(matrix[0]))] for i in range(len(matrix))]
        maxSeen = any([any([a=='1' for a in row]) for row in matrix])
        # print(maxSeen)
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                    maxSeen = max(maxSeen, dp[i][j])
        # print(dp)
        return maxSeen*maxSeen