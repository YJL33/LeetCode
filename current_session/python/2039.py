from typing import List
import collections
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        # simply simulate the process
        # craft adj list
        # we want to know the distance to 0
        adj = collections.defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        # BFS-like
        # each node will stop sending after receive the 1st response
        q = collections.deque()
        q.append((0,0))
        dist = {0:0}
        max_idle_time = float('-inf')

        # from L23-27 we know that we will only check each node once
        # can be re-factored into O(n) like structure
        while q:
            x, d = q.popleft()
            for y in adj[x]:
                if y not in dist:
                    D, P = d+1, patience[y]
                    q.append((y, D))
                    dist[y] = D
                    local_idle = P*(((2*D)-1)//P) + 2*D
                    max_idle_time = max(max_idle_time, local_idle)

        return max_idle_time+1

