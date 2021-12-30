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

    def longestIncreasingPath_redo(self, matrix: List[List[int]]) -> int:
        # DFS
        self.visited = {}
        def dfs(i, j):
            # update the maxSeen while no more moves
            if (i,j) in self.visited: return self.visited[(i,j)]
            road_ahead = []
            for a, b in [(i+1, j), (i-1, j), (i,j+1), (i,j-1)]:
                if 0<=a<len(matrix) and 0<=b<len(matrix[0]) and matrix[a][b] > matrix[i][j]:
                    road_ahead.append(dfs(a, b))
            if len(road_ahead) == 0:
                self.visited[(i,j)] = 1
            else:
                self.visited[(i,j)] = 1+max(road_ahead)
            return self.visited[(i,j)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j)
        
        return max(self.visited.values())

print(Solution().longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
print(Solution().longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
print(Solution().longestIncreasingPath([[1]]))
print(Solution().longestIncreasingPath([[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]))
print(Solution().longestIncreasingPath([[1,2]]))