import collections
from typing import List
class Solution:
    # thoughts
    # user DP? (hard to handle if the shortest path includes up and down, or left and right)
    # use BFS, starting from top-left, put it into deque, and add all possible neighbors into dq
    # optimization: modify the grid so we can save 'visited'
    #
    # analysis
    # tc: O(P) where P is the length of shortest path, worst case O(H*W)
    # sc: O(D) where D is the size of deque
    # e.g. [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
    #
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        H, W = len(grid), len(grid[0])

        dq = collections.deque([(0,0,1)])
        
        while dq:
            i, j, l = dq.popleft()
            if (i == H-1 and j == W-1): return l
            for p, q in [(i+1,j+1), (i+1,j), (i+1,j-1), (i,j+1), (i,j-1), (i-1,j+1), (i-1,j), (i-1,j-1)]:
                if 0<=p<H and 0<=q<H and grid[p][q] == 0 and l+1<H*W:
                    grid[p][q] = -1
                    dq.append((p,q,l+1))
        return -1

print(Solution().shortestPathBinaryMatrix([[0,1,1,0,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],[0,0,0,1,1,0],[1,1,1,1,1,0],[1,1,1,1,1,0]]))
print(Solution().shortestPathBinaryMatrix([[0,1,1,1,1,1,1,1],[0,1,1,0,0,0,0,0],[0,1,0,1,1,1,1,0],[0,1,0,1,1,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,1,1,0,1,0],[0,0,0,0,0,1,1,0],[1,1,1,1,1,1,1,0]]))
print(Solution().shortestPathBinaryMatrix([[0,1,0,0,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],[0,0,0,0,1,0],[1,1,1,1,1,0],[1,1,1,1,1,0]]))