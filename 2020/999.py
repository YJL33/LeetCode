"""
see https://leetcode.com/problems/rotting-oranges/
"""
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # check through all grids to see if there exists any:
        # a. fresh orange that adjacent to no rotten ones
        # b. any fresh orange

        # for r in grid: print(r)

        freshCnt = 0
        for r in grid:
            freshCnt += r.count(1)

        if freshCnt == 0: return 0

        res = 0
        while freshCnt != 0:
            grid, rottenCnt = self.after1min(grid)
            if rottenCnt == 0: return -1
            res, freshCnt = res+1, freshCnt-rottenCnt

        return res


    def after1min(self, grid):
        """
        update the grid and return the rotten oranges in next min
        """
        rot = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    coordinates = [(0,1),(1,0),(-1,0),(0,-1)]
                    for c in coordinates:
                        if 0<=i+c[0] and i+c[0]<len(grid) and 0<=j+c[1] and j+c[1]<len(grid[0]):
                            if (i+c[0], j+c[1]) not in rot and grid[i+c[0]][j+c[1]] == 1:
                                rot.add((i+c[0], j+c[1]))

        for c in rot:
            grid[c[0]][c[1]] = 2

        return grid, len(rot)


print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(Solution().orangesRotting([[2,0,0],[0,2,2],[2,0,2]]))
