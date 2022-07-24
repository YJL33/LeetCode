from typing import List
import heapq
import collections
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # times[i] = (u, v, w), where w is the time needed from u to v
        # send a signal from given node k
        # return the time needed for all n nodes to receive the signal
        # if impossible for all n nodes, return -1
        # 
        # this is directed graph
        # 
        # simply use DFS?
        # craft adj list O(E)
        # start from the starting node, and visit all possible nodes O(N)
        # store the visited node, and update the earliest receiving time
        # analysis:
        # tc: O(E) to make adj list, O(size of stack) to use all (possible) edges, worst case O(E)
        # sc: O(E) for adj list, O(size of stack), O(N) for visited nodes
        #
        # use Dijkstra
        # similarly, craft adj list first
        # but use min Heap instead of stack
        # No need to visit any node twice.
        # analysis:
        # tc: O(E) to make adj list, O(NlogH) to visit all nodes, where H is the size of heap, worst case O(NlogN)
        # sc: O(E) for adj list, O(size of heap), O(N) for visited nodes
        
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v,w))
        
        visited = {}
        max_time = 0
        minHp = [(0, k)]
        while minHp:
            time, node = heapq.heappop(minHp)
            if node not in visited:
                visited[node] = time
                for nb, t in adj[node]:
                    heapq.heappush(minHp,(time+t, nb))

        if len(visited) != n: return -1
        return max([v for v in visited.values()])
                