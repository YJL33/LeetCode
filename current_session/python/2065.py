from typing import List
import collections
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        # simply do DFS and update max value for valid paths
        # craft adj list
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            a, b, val = edges[i]
            adj[a].append((b, val))
            adj[b].append((a, val))
        
        self.maxSeen = float('-inf')

        def dfs(node, visited, time_spent=0):
            # end if no enough time to go back
            if time_spent > maxTime: return
            if node == 0:
                # print('visited:', visited, time_spent)
                self.maxSeen = max(self.maxSeen, sum([values[p] for p, v in visited.items() if v != 0]))
            for nb, cost in adj[node]:
                visited[nb] += 1
                dfs(nb, visited, time_spent+cost)
                visited[nb] -= 1
            return
            
        visited = collections.Counter()
        visited[0] += 1
        dfs(0, visited)
        return self.maxSeen

print(Solution().maximalPathQuality(values = [0,32,10,43], edges = [[0,1,10],[1,2,15],[0,3,10]], maxTime = 49))
print(Solution().maximalPathQuality(values = [5,10,15,20], edges = [[0,1,10],[1,2,10],[0,3,10]], maxTime = 30))
print(Solution().maximalPathQuality(values = [1,2,3,4], edges = [[0,1,10],[1,2,11],[2,3,12],[1,3,13]], maxTime = 50))