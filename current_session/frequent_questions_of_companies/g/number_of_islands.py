from typing import List
class Solution:
    def numIslands(self, grid:List[List[str]]) -> int:
        H, W = len(grid), len(grid[0])

        def dfs(i, j):
            # modify grid in-place
            grid[i][j] = '0'
            for a, b in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0<=a<H and 0<=b<W and grid[a][b] == '1':
                    dfs(a, b)
            grid[i][j] = '2'
            return

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    cnt += 1
        
        print(grid)
        return cnt

print(Solution().numIslands([['1','1','0','0'],['0','0','0','0'],['1','1','0','0'],['0','0','1','1']]))