from typing import List
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        nodeColor = {}          # key: node, value: color

        def dfs(node):
            if node not in nodeColor:
                nodeColor[node] = 1
            for n in graph[node]:
                if n not in nodeColor:
                    nodeColor[n] = -1*nodeColor[node]
                    if not dfs(n):
                        return False
                else:
                    if nodeColor[n] == nodeColor[node]:
                        return False
            return True
        
        for node in range(len(graph)):
            if not dfs(node):
                return False
        
        return True
