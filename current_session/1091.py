"""
1091
"""
from typing import List
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # BFS
        # start from 'end'
        # move to nb and +1 if see neighbor = 0
        # finish until we see 0, 0

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        n = len(grid)
        self.seen = [[-1 for _ in range(n)] for _ in range(n)]
        stack = [(n-1,n-1,1)]
        outer = 0
        while stack and outer < n**n:
            tmp = []            # next layer
            # stack.pop()
            for i,j,cnt in stack:
                if i==j==0:
                    return cnt
                for ni, nj in [(i+1,j+1),(i+1,j),(i+1,j-1),(i,j+1),(i,j-1),(i-1,j+1),(i-1,j),(i-1,j-1)]:
                    if 0<=ni<n and 0<=nj<n and grid[ni][nj] == 0 and self.seen[ni][nj] == -1:
                        self.seen[ni][nj] = 1
                        tmp += (ni,nj,cnt+1),
            stack = tmp
            outer += 1

        return -1
                    
print(Solution().shortestPathBinaryMatrix([[0,1,1,0,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],[0,0,0,1,1,0],[1,1,1,1,1,0],[1,1,1,1,1,0]]))
print(Solution().shortestPathBinaryMatrix([[0,1,1,1,1,1,1,1],[0,1,1,0,0,0,0,0],[0,1,0,1,1,1,1,0],[0,1,0,1,1,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,1,1,0,1,0],[0,0,0,0,0,1,1,0],[1,1,1,1,1,1,1,0]]))