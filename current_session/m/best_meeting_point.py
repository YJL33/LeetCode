from typing import List

# median should minimize the distance
# e.g. (1,0), (0,5) => (0.5, 2.5)
# time analysis:
# go through the whole grid: O(H*W)
# sort => O(NlogN), where N is the number of 1s
# find distance: O(N)

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:

        H, W = len(grid), len(grid[0])

        rows, cols = [], []
        for i in range(H):
            for j in range(W):
                if grid[i][j] == 1:
                    rows += i,
                    cols += j,
        rows.sort()
        cols.sort()
        
        def findDistance(rows, cols, k):
            a, b = rows[k], cols[k]
            dist = 0
            for i in range(H):
                for j in range(W):
                    if grid[i][j] == 1:
                        dist += abs(i-a) + abs(j-b)
            return dist

        L = len(rows)
        if L%2:
            return findDistance(rows, cols, L//2)
        else:
            return 0.5*(findDistance(rows, cols, L//2) + findDistance(rows, cols, (L//2)-1))
