from typing import List
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # use dfs + heap
        # time analysis
        # operation of heappop and heappush: O(logN)
        # visited all heights: O(N)
        # overall: O(NlogN), where N is the size of given heights (H*W)

        H, W = len(heights), len(heights[0])
        hp = [(0,0,0)]      # diff, i, j
        effort = 0
        visited = set()

        while hp:
            diff, i, j = heapq.heappop(hp)
            
            effort = max(effort, diff)
            if i == H-1 and j == W-1:
                return effort

            visited.add(i,j)
            for a, b in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0<=a<H and 0<=b<W and (a,b) not in visited:
                    newDiff = abs(heights[a][b]-heights[i][j])
                    heapq.heappush((newDiff, a, b))
        
        # when reach here?
        return effort