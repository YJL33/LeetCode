from typing import List
from collections import defaultdict
import math
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # do DFS(?)
        bd = defaultdict(list)
        for i in range(len(bombs)):
            x, y, r = bombs[i]
            for j in range(i+1, len(bombs)):
                x2, y2, r2 = bombs[j]
                dist = self.getDist(x, y, x2, y2)
                if dist <= r:
                    bd[i].append(j)
                if dist <= r2:
                    bd[j].append(i)
        
        def dfs(i, visited):
            visited.add(i)
            cnt = 1
            for nb in bd[i]:
                if nb not in visited:
                    cnt += dfs(nb, visited)
            return cnt
        
        maxSeen = 0
        for i in range(len(bombs)):
            maxSeen = max(maxSeen , dfs(i, set()))
        return maxSeen
    
    def getDist(self, x1, y1, x2, y2):
        return math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))

print(Solution().maximumDetonation([[2,1,3],[6,1,4]]))
print(Solution().maximumDetonation([[1,1,5],[10,10,5]]))
print(Solution().maximumDetonation([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))