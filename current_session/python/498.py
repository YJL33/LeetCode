"""
498
"""
from typing import List
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        H, W = len(mat), len(mat[0])
        # either do (i+1, j-1), (i-1, j+1), (i+1, j), (i, j+1)
        diag = [(1,-1), (-1,1)]             # move along diagonal
        nxt = [(1,0), (0,1)]                # next diagonal, either i+1 or j+1
        i, j, d, n = 0, 0, -1, -1
        res = []
        while len(res) < H*W:
            res += mat[i][j],
            di, dj = diag[d]
            if i+di < 0 or i+di >= H or j+dj < 0 or j+dj >= W:                  # next diag
                if d == 0: n = 0 if (i+1) < H else 1
                else: n = 1 if (j+1) < W else 0
                di, dj, d = nxt[n][0], nxt[n][1], (d+1)%2
            i, j = i+di, j+dj
        return res

print(Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().findDiagonalOrder([[1,2,3,10],[4,5,6,10],[7,8,9,10]]))
print(Solution().findDiagonalOrder([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))
