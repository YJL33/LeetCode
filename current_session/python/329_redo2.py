from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # use a dict to store visited longest path of (i, j)
        seen = {}
        H, W = len(matrix), len(matrix[0])
        def find(i, j):
            if (i, j) in seen:
                return seen[(i,j)]
            longest = 1
            for a, b in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0<=a<H and 0<=b<W and matrix[a][b] > matrix[i][j]:
                    l = find(a,b)
                    longest = max(longest, 1+l)
            seen[(i,j)] = longest
            return longest
        for i in range(H):
            for j in range(W):
                find(i, j)
        
        return max([v for _, v in seen.items()])

print(Solution().longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
print(Solution().longestIncreasingPath([[1,2]]))