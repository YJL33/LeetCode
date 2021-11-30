from typing import List
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        if not mat: return 0
        H, W = len(mat), len(mat[0])
        maxSeen = 0
        # calculate horizontal
        for i in range(H):
            prev = 0
            for j in range(W):
                prev = prev+1 if mat[i][j] == 1 else 0
                maxSeen = max(maxSeen, prev)
        # calculate vertical
        for j in range(W):
            prev = 0
            for i in range(H):
                prev = prev+1 if mat[i][j] == 1 else 0
                maxSeen = max(maxSeen, prev)

        def finder(i, j, di, dj):
            self.visited.add((i,j))
            if 0<=i+di<H and 0<=j+dj<W and mat[i+di][j+dj] == 1:
                return 1+finder(i+di, j+dj, di, dj)
            else:
                return 1

        # calculate diagonal
        self.visited = set()
        for i in range(H):
            for j in range(W):
                if mat[i][j] == 1 and (i,j) not in self.visited:
                    maxSeen = max(maxSeen, finder(i, j, 1, 1))
        
        # calculate anti-diag, reset visited
        self.visited = set()
        for i in range(H):
            for j in range(W):
                if mat[i][j] == 1 and (i,j) not in self.visited:
                    maxSeen = max(maxSeen, finder(i, j, 1, -1))
        
        return maxSeen

print(Solution().longestLine([[0,1,1,0],[0,1,1,0],[0,0,0,1]]))
print(Solution().longestLine([[1,1,1,1],[0,1,1,0],[0,0,0,1]]))