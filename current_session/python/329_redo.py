from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: return 0
        H, W = len(matrix), len(matrix[0])

        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                u = dfs(i-1, j) if i-1 >=0 and matrix[i-1][j] > val else 0
                d = dfs(i+1, j) if i+1 < H and matrix[i+1][j] > val else 0
                l = dfs(i, j-1) if j-1 >=0 and matrix[i][j-1] > val else 0
                r = dfs(i, j+1) if j+1 < W and matrix[i][j+1] > val else 0
                dp[i][j] = max([u,d,l,r])+1
            return dp[i][j]
        
        dp = [[0 for _ in range(W)] for _ in range(H)]
        return max(dfs(i,j) for i in range(H) for j in range(W))

print(Solution().longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
print(Solution().longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
print(Solution().longestIncreasingPath([[1]]))
print(Solution().longestIncreasingPath([[1,2]]))