from typing import List
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # use DP
        # dp[i] is the max cherry that robot can collect
        # base: [row[0], 0,0,0.... row[-1]] where row is the first row of grid
        # need to consider overlapping case
        #
        H, W = len(grid), len(grid[0])
        if W == 2: return sum([sum(row) for row in grid])
        r1 = [grid[0][0]] + [0 for _ in grid[0][1:]]
        r2 = [0 for _ in grid[0][:-1]] + [grid[0][-1]]
        for i in range(1,H):
            t1, t2 = [0 for _ in range(W)], [0 for _ in range(W)]
            # for j in range(W):
            #     if r1[j] != 0:
            #         if j-1 > 0: t1[j-1] = max(t1[j-1], grid[i][j-1]+r1[j])
            #         if j+1 < W: t1[j+1] = max(t1[j+1], grid[i][j+1]+r1[j])
            #         t1[j] = max(grid[i][j]+r1[j], t1[j])
            #     if r2[j] != 0:
            #         if j-1 > 0: t2[j-1] = max(t2[j-1], grid[i][j-1]+r2[j])
            #         if j+1 < W: t2[j+1] = max(t2[j+1], grid[i][j+1]+r2[j])
            #         t2[j] = max(grid[i][j]+r2[j], t2[j])
            print('r1:', t1)
            r1, r2 = t1, t2
        return max(r1)+max(r2)

print(Solution().cherryPickup([[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]))