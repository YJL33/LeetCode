from typing import List
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # first sink those islands connected with edge
        # then count the number of islands

        H, W = len(grid), len(grid[0])

        def sink(i, j):
            grid[i][j] = 1      # sink it
            for a, b in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0<=a<H and 0<=b<W and grid[a][b] == 0:
                    sink(a, b)
            return
            
        for i in range(H):
            if grid[i][0] == 0: sink(i, 0)
            if grid[i][W-1] == 0: sink(i, W-1)
        
        for j in range(W):
            if grid[0][j] == 0: sink(0, j)
            if grid[H-1][j] == 0: sink(H-1, j)

        cnt = 0
        for i in range(1, H-1):
            for j in range(1, W-1):
                if grid[i][j] == 0:
                    cnt += 1
                    sink(i, j)
        
        return cnt