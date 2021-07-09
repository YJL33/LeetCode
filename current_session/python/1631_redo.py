"""
1631
"""
from typing import List
import heapq
class Solution:
    def minimumEffortPath(self, A: List[List[int]]) -> int:
        # Dijkstra
        # psuedo code:
        # for each point
        # visit each of its 'unvisited' neighbor and update the nb's effort
        # if updated, store nb's prev
        # return eff of target when visit the target

        visited = set()
        unvisited = [(0,0,0)]
        eff = [[float('inf') for _ in A[0]] for _ in A]
        eff[0][0] = 0

        res = 0

        while unvisited:
            e, i, j = heapq.heappop(unvisited)
            res = max(res, e)
            if (i,j) == (len(A)-1, len(A[0])-1):
                return res
            nbs = [(1,0),(-1,0),(0,1),(0,-1)]
            for nb in nbs:
                x, y = i+nb[0], j+nb[1]
                if 0 <= x < len(A) and 0 <= y < len(A[0]) and (x,y) not in visited:
                    val = eff[x][y]
                    diff = abs(A[x][y]-A[i][j])
                    if diff < val:
                        eff[x][y] = diff
                    heapq.heappush(unvisited, (eff[x][y],x,y))
            visited.add((i, j))
            
        return res

print(Solution().minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))
print(Solution().minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]))
print(Solution().minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))
print(Solution().minimumEffortPath([[1,10,6,7,9,10,4,9]]))
print(Solution().minimumEffortPath([[4,3,4,10,5,5,9,2],[10,8,2,10,9,7,5,6],[5,8,10,10,10,7,4,2],[5,1,3,1,1,3,1,9],[6,4,10,6,10,9,4,6]]))

