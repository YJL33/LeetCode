"""
Kosaraju

given direct graph, find critical edges(bridges)
"""
import collections
from typing import List
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # find strongly connected components
        # list all edges that connect two different sccs

        # build adjacency list
        nd = collections.defaultdict(list)
        rnd = collections.defaultdict(list)
        for c in connections:
            nd[c[0]].append(c[1])
            rnd[c[1]].append(c[0])
        
        # dfs1
        visited = [False for _ in range(n)]
        stack = []
        
        def dfs1(i):
            visited[i] = True
            for x in nd[i]:
                if not visited[x]:
                    dfs1(x)
            stack.append(i)

        for i in range(n):
            if not visited[i]:
                dfs1(i)
        
        # dfs2
        visited2 = [False for _ in range(n)]
        who = [-1 for _ in range(n)]

        def dfs2(i, rep):
            visited2[i] = True
            who[i] = rep
            for x in rnd[i]:
                if not visited2[x]:
                    dfs2(x, rep)

        while stack:
            n = stack.pop()
            if not visited2[n]:
                dfs2(n, n)
        
        # print(nd)
        # print(rnd)
        # print(stack)
        print(who)

        # who[i] is the representative node of i
        res = []
        for c in connections:
            if who[c[0]] != who[c[1]]:
                res += c,
        return res

print(Solution().criticalConnections(n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]))
print(Solution().criticalConnections(5, [[1,0],[2,0],[3,2],[4,2],[4,3],[3,0],[4,0]]))