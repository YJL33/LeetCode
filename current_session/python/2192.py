from typing import List
import collections
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # use DFS       
        # given n -> we know the number of nodes
        # with adj list, it'll be easier to track visited or not
        res = [set() for _ in range(n)]
        
        adj = collections.defaultdict(list)
        for a, b in edges:
            adj[b].append(a)
        
        self.visited = set()
        
        def dfs(i):
            if i in self.visited:
                return res[i]
            self.visited.add(i)
            for nb in adj[i]:
                if nb not in self.visited:
                    dfs(nb)
                res[i].add(nb)
                res[i] = res[i].union(res[nb])
            return res[i]
            
        for i in range(n):
            if i not in adj:
                self.visited.add(i)
            else:
                dfs(i)
        
        return [sorted(r) for r in res]