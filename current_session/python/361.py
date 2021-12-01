from typing import List
class Solution:
    def maxKilledEnemies(self, grid):
        if len(grid) == 0: return 0
        max_hits = 0
        nums = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        #From Left
        for i in range(len(grid)):
            row_hits = 0
            for j in range(len(grid[0])):
                if grid[i][j] == 'E': row_hits += 1
                elif grid[i][j] == 'W': row_hits = 0
                else: nums[i][j] = row_hits
                
        #From Right
        for i in range(len(grid)):
            row_hits = 0
            for j in range(len(grid[0])-1, -1, -1):
                if grid[i][j] == 'W': row_hits = 0
                elif grid[i][j] == 'E': row_hits +=1
                else: nums[i][j] += row_hits

        for i in range(len(nums[0])):
            col_hits = 0
            for col in range(len(nums)):
                if grid[col][i] == 'E': col_hits += 1
                elif grid[col][i] == 'W': col_hits = 0
                else: nums[col][i] += col_hits

        for i in range(len(nums[0])):
            col_hits = 0
            for col in range(len(nums)-1, -1, -1):
                if grid[col][i] == 'E': col_hits +=1
                elif grid[col][i] == 'W': col_hits = 0
                else:
                    nums[col][i] = nums[col][i]+col_hits
                    max_hits = max(max_hits, nums[col][i]+col_hits)

        return max_hits

    def maxKilledEnemies_MEMO(self, grid: List[List[str]]) -> int:
        # memoization: 5%
        # for each grid, store 4 directions if visited
        H, W = len(grid), len(grid[0])

        self.visited = [[[-1,-1,-1,-1] for _ in range(W)] for _ in range(H)]
        self.dir = [[1,0], [0,1], [-1,0], [0,-1]]

        def count(i, j):
            # check 4 directions
            a = checker(i+1, j, 0)
            b = checker(i, j+1, 1)
            c = checker(i-1, j, 2)
            d = checker(i, j-1, 3)
            return a+b+c+d
        
        def checker(i, j, d):
            di, dj = self.dir[d]
            if 0<=i<H and 0<=j<W and grid[i][j] != 'W':
                if self.visited[i][j][d] != -1: return self.visited[i][j][d]
                res = checker(i+di, j+dj, d)
                if grid[i][j] == 'E': res += 1
                self.visited[i][j][d] = res
                return res
            else:
                return 0

        ans = 0
        for i in range(H):
            for j in range(W):
                if grid[i][j] == '0':
                    killed = count(i, j)
                    ans = max(ans, killed)
        return ans

print(Solution().maxKilledEnemies([["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]))
print(Solution().maxKilledEnemies([["W","W","W"],["0","0","0"],["E","E","E"]]))