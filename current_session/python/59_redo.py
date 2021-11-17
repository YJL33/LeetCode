from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[-1 for _ in range(n)] for _ in range(n)]
        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        d = 0
        cnt = 0
        pos = (0,0)

        def isValid(r, c):
            return (0<=r<n and 0<=c<n and grid[r][c] == -1)

        while cnt < n*n:
            i, j = pos
            grid[i][j] = cnt+1
            cnt += 1
            if cnt == n*n: break
            
            di, dj = dir[d%4]
            while not isValid(i+di, j+dj):
                d += 1
                di, dj = dir[d%4]
            pos = (i+di, j+dj)
        return grid

print(Solution().generateMatrix(5))