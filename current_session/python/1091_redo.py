import collections
class Solution:
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        H = len(grid)
        # use BFS
        dq = collections.deque()
        dq.append((0,0,1))
        k = 0
        while dq and k < H*H:
            i, j, c = dq.popleft()
            if (i == H-1) and (j == H-1): return c
            for p, q in [(i+1,j+1), (i+1,j), (i+1,j-1), (i,j+1), (i,j-1), (i-1,j+1), (i-1,j), (i-1,j-1)]:
                if 0<=p<H and 0<=q<H and grid[p][q] == 0 and c+1<H*H:
                    grid[p][q] = -1
                    dq.append((p,q,c+1))
            k += 1
        return -1

print(Solution().shortestPathBinaryMatrix([[0,1,1,0,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],[0,0,0,1,1,0],[1,1,1,1,1,0],[1,1,1,1,1,0]]))
print(Solution().shortestPathBinaryMatrix([[0,1,1,1,1,1,1,1],[0,1,1,0,0,0,0,0],[0,1,0,1,1,1,1,0],[0,1,0,1,1,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,1,1,0,1,0],[0,0,0,0,0,1,1,0],[1,1,1,1,1,1,1,0]]))
print(Solution().shortestPathBinaryMatrix([[0,1,0,0,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],[0,0,0,0,1,0],[1,1,1,1,1,0],[1,1,1,1,1,0]]))