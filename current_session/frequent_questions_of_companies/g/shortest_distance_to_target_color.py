from typing import List
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        
        nearest = [[float('inf'),float('inf'),float('inf'),float('inf')] for _ in colors]
        prev = [float('inf'),float('inf'),float('inf'),float('inf')]
        # fill itself into nearest
        # fill from left side
        for i in range(len(colors)):
            c = colors[i]
            nearest[i][c] = 0
            for cc in [1,2,3]:
                if prev[cc] != float('inf') and cc != c:
                    nearest[i][cc] = i-prev[cc]
            prev[c] = i
        
        # fill from right side
        prev = [float('inf'),float('inf'),float('inf'),float('inf')]
        for i in range(len(colors)-1, -1, -1):
            c = colors[i]
            for cc in [1,2,3]:
                if prev[cc] != float('inf') and cc != c:
                    nearest[i][cc] = min(nearest[i][cc], prev[cc]-i)
            prev[c] = i
        # print(nearest)

        res = []
        for i, c in queries:
            x = nearest[i][c]
            if x != float('inf'):
                res.append(x)
            else:
                res.append(-1)
        return res
        
print(Solution().shortestDistanceColor([1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]))
print(Solution().shortestDistanceColor(colors = [1,2], queries = [[0,3]]))