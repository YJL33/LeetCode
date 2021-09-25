# analysis: DFS from each grid
# time complexity: O(HW*HW) => need a smarter pruning
# 
from typing import List
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        H, W = len(grid), len(grid[0])
        self.maxGold = 0
        
        def dfs(i, j, pathSum, visited):
            pathSum += grid[i][j]
            if pathSum > self.maxGold:
                self.maxGold = pathSum
            
            for a, b in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=a<H and 0<=b<W and grid[a][b] != 0 and (a,b) not in visited:
                    visited.add((a,b))
                    dfs(a,b,pathSum,visited)
                    visited.remove((a,b))
            return

        for i in range(H):
            for j in range(W):
                if grid[i][j] != 0:
                    start = set()
                    start.add((i,j))
                    dfs(i, j, 0, start)
        return self.maxGold

print(Solution().getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]))
print(Solution().getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))
print(Solution().getMaximumGold([[1,0,7,0,0,0],[2,0,6,0,1,0],[3,5,6,7,4,2],[4,3,1,0,2,0],[3,0,5,0,20,0]]))
