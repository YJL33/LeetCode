from typing import List
from collections import defaultdict

# dfs solution
# is it possible to get the result by finding the critical node (articulation point)?
class Solution:
    def findMinHeightTrees(self, n: int, E: List[List[int]]) -> List[int]:
        G, seen = defaultdict(set), [False]*n
        for u,v in E:
            G[u].add(v)
            G[v].add(u)

        def dfs(i):
            if seen[i]: return []
            seen[i] = True
            longest_path = max((dfs(adj) for adj in G[i]), key=len, default=[]) + [i]
            seen[i] = False
            return longest_path

        path = dfs(dfs(0)[0])
        return set([path[len(path)//2], path[(len(path)-1)//2]])