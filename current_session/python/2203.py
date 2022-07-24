from typing import List
from collections import defaultdict
from heapq import heappop, heappush
class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], s1: int, s2: int, dest: int) -> int:

        adj = defaultdict(list)
        rev = defaultdict(list)
        for a, b, w in edges:
            adj[a].append((b, w))
            rev[b].append((a, w))

        # return min_time array (from start)
        # update along time, skip those visited earlier
        def dijkstra(graph, start):
            pq, min_time = [(0, start)], {}
            while pq:
                time, node = heappop(pq)
                if node not in min_time:
                    min_time[node] = time
                    for v, w in graph[node]:
                        heappush(pq, (time + w, v))
            return [min_time[i] if i in min_time else float("inf") for i in range(n)]

        arr1 = dijkstra(adj, s1)
        arr2 = dijkstra(adj, s2)
        arr3 = dijkstra(rev, dest)

        ans = float("inf")
        for i in range(n):
            ans = min(ans, arr1[i] + arr2[i] + arr3[i])
        
        return ans if ans != float("inf") else -1
