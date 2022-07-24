from typing import List
import collections
class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:      
        # use bfs
        self.items = collections.defaultdict(list)
        self.cnt = 0
        max_dist = 0
        visited = set()
        upper, lower, dist = pricing[1], pricing[0], 0
        H, W = len(grid), len(grid[0])
        dq = collections.deque()
        dq.append(start+[0])
        while dq and (self.cnt < k or dq[0][-1] == max_dist):
            a, b, dist = dq.popleft()
            if (a,b) in visited:
                continue
            visited.add((a,b))
            if lower <= grid[a][b] <= upper:
                self.items[dist].append([grid[a][b],a,b])
                self.cnt += 1
                max_dist = max(max_dist, dist)
            
            if a-1 >= 0 and grid[a-1][b] != 0:
                dq.append([a-1, b, dist+1])
            if b-1 >= 0 and grid[a][b-1] != 0:
                dq.append([a, b-1, dist+1])
            if b+1 < W and grid[a][b+1] != 0:
                dq.append([a, b+1, dist+1])
            if a+1 < H and grid[a+1][b] != 0:
                dq.append([a+1, b, dist+1])
        
        res = []
        for i in range(max_dist+1):
            if i in self.items:
                v = self.items[i]
                v.sort()
                res += [[x[1], x[2]] for x in v]

        return res[:k]