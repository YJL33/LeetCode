"""
see https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
"""
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # dp from everypoint + dp
        if not matrix or not matrix[0]: return 0
        h, w = len(matrix), len(matrix[0])

        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                # print(" i: ", i, " j: ", j, " val: ", val)
                up = dfs(i-1, j) if i-1 >= 0 and val > matrix[i-1][j] else 0
                down = dfs(i+1, j) if i+1 < h and val > matrix[i+1][j] else 0
                left = dfs(i, j-1) if j-1 >= 0 and val > matrix[i][j-1] else 0
                right = dfs(i, j+1) if j+1 < w and val > matrix[i][j+1] else 0
                dp[i][j] = 1 + max(up, down, left, right)
            return dp[i][j]
        
        dp = [[0 for _ in range(w)] for _ in range(h)]
        return max(dfs(i, j) for j in range(w) for i in range(h))

print(Solution().longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
print(Solution().longestIncreasingPath([[1,2]]))