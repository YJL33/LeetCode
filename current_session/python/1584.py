from typing import List
import heapq
import collections
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # clarification / notes
        # cost to collect a, b: manhattan_dist(a, b)
        # to connect N points: we need N-1 edges, if there's no copoint
        # input validity? (co-points?)
        # 
        # thoughts:
        # if every point is connected to the point that closest to it, is it the case? NO
        #
        # brute force:
        # list all distance between i, j
        # we can't pick the closet point to it for all i, j, because all points needs to be connected
        #
        # use heap, and maintain the visit state of each point.
        # squash all distances into a heap, pop out until there's no more points needs to be covered
        #
        # tc: O(n^2) to calculate all distances, O(nlogn) for heap operations
        # sc: O(n)

        # manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        def dist(x1, y1, x2, y2): return abs(x1-x2)+abs(y1-y2)

        n, ddict = len(points), collections.defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                d = dist(points[i][0], points[i][1], points[j][0], points[j][1])
                ddict[i].append((d, j))
                ddict[j].append((d, i))

        cnt, ans, visited, hp = 1, 0, [0]*n, [(d, idx) for d, idx in ddict[0]]
        visited[0] = 1
        heapq.heapify(hp)
        while hp:
            d, j = heapq.heappop(hp)
            if not visited[j]:
                visited[j], cnt, ans = 1, cnt+1, ans+d
                for nxt_d, nxt_j in ddict[j]:
                    heapq.heappush(hp, (nxt_d, nxt_j))
            if cnt >= n: break        
        return ans
        